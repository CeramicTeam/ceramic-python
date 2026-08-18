import os
import asyncio
from typing import Type, Mapping, Callable, Optional, Awaitable, cast

from ceramic_ai import AsyncCeramic
from ceramic_ai._exceptions import (
    CeramicError,
    APIStatusError,
    AuthenticationError,
    UnprocessableEntityError,
)

# ---------------------------
# Helpers
# ---------------------------

test_passed = 0
test_failed = 0


def ok(label: str) -> None:
    global test_passed
    test_passed += 1
    print(f"✅ {label}")


def bad(label: str, msg: str = "") -> None:
    global test_failed
    test_failed += 1
    print(f"❌ {label}")
    if msg:
        print("   " + msg)


async def expect_ok(label: str, fn: Callable[[], Awaitable[object]]) -> None:
    """✅ if await fn() succeeds, ❌ if it raises."""
    try:
        await fn()
        ok(label)
    except Exception as e:
        bad(label, f"got {type(e).__name__}: {e}")

async def expect_validation_error(label: str, fn: Callable[[], Awaitable[object]]) -> None:
    try:
        await fn()
        bad(label, "unexpected success (expected a validation error)")
    except CeramicError as e:
        ok(label)
    except Exception as e:
        bad(label, f"wrong exception: expected CeramicError, got {type(e).__name__}: {e}")
        
async def expect_api_error(
    label: str,
    fn: Callable[[], Awaitable[object]],
    *,
    status: Optional[int] = None,
    code: Optional[str] = None,
    exc: Type[APIStatusError] = APIStatusError,
) -> None:
    """
    ✅ if await fn() raises the expected API error (and optionally matches status/code),
    ❌ otherwise.
    """
    try:
        await fn()
        bad(label, "unexpected success (expected an error)")
    except Exception as e:
        if not isinstance(e, exc):
            bad(label, f"wrong exception: expected {exc.__name__}, got {type(e).__name__}")
            return

        # status_code may or may not exist; treat as Optional[int]
        got_status = cast(Optional[int], getattr(e, "status_code", None))

        # body may be dict-like or something else; normalize to Mapping[str, object]
        body_raw = getattr(e, "body", None)
        body: Mapping[str, object]
        if isinstance(body_raw, dict):
            body = cast(Mapping[str, object], body_raw)
        else:
            body = {}

        got_code_obj = body.get("code")
        got_code = got_code_obj if isinstance(got_code_obj, str) else None

        if status is not None and got_status != status:
            bad(label, f"wrong status: expected {status}, got {got_status} body={dict(body)}")
            return
        if code is not None and got_code != code:
            bad(label, f"wrong code: expected {code!r}, got {got_code!r} body={dict(body)}")
            return

        ok(label)


def make_client(api_key: Optional[str] = None) -> AsyncCeramic:
    """
    Create an AsyncCeramic client. Uses CERAMIC_API_KEY if api_key is not provided.
    """
    return AsyncCeramic(
        api_key=api_key or os.environ["CERAMIC_API_KEY"],
        base_url="https://api.ceramic.ai/",
    )

# ---------------------------
# Tests
# ---------------------------

async def ex_basic_query() -> None:
    client = make_client()
    await expect_ok("basic query", lambda: client.search(query="California rental laws"))

async def ex_invalid_api_key() -> None:
    client = make_client(api_key="invalid_api_key")
    await expect_api_error(
        "invalid api key",
        lambda: client.search(query="test invalid key"),
        status=401,
        code="invalid_api_key",
        exc=AuthenticationError,
    )

async def ex_query_validation() -> None:
    client = make_client()
    await expect_validation_error("query: too many words", lambda: client.search(query=" ".join(["word"] * 51)))
    await expect_validation_error("query: blank",          lambda: client.search(query="   "))

async def ex_max_results_validations() -> None:
    client = make_client()

    cases = [
        ("zero",          0,  False),
        ("negative",      -1, False),
        ("valid_min",     1,  True),
        ("valid_default", 10, True),
        ("valid_max",     50, True),
        ("above_max",     51, False),
    ]

    for name, mr, is_valid in cases:
        label = f"max_results validation: {name} (max_results={mr})"
        if is_valid:
            await expect_ok(label, lambda mr=mr: client.search(query="rate limits and retries", max_results=mr))
        else:
            await expect_api_error(
                label,
                lambda mr=mr: client.search(query="rate limits and retries", max_results=mr),
                status=422,
                code="invalid_parameter",
                exc=UnprocessableEntityError,
            )

async def ex_max_description_length_validations() -> None:
    client = make_client()

    cases = [
        ("zero",          0,    False),
        ("below_min",     999,  False),
        ("valid_min",     1000, True),
        ("valid_default", 3000, True),
        ("above_max",     8001, False),
    ]

    for name, mdl, is_valid in cases:
        label = f"max_description_length validation: {name} (max_description_length={mdl})"
        if is_valid:
            await expect_ok(label, lambda mdl=mdl: client.search(query="rate limits and retries", max_description_length=mdl))
        else:
            await expect_api_error(
                label,
                lambda mdl=mdl: client.search(query="rate limits and retries", max_description_length=mdl),
                status=422,
                code="invalid_parameter",
                exc=UnprocessableEntityError,
            )


async def main() -> None:
    try:
        await ex_basic_query()
        await ex_invalid_api_key()
        await ex_query_validation()
        await ex_max_results_validations()
        await ex_max_description_length_validations()
    except CeramicError as e:
        print("\nCeramic SDK error (not an API status error):")
        print(str(e))
    finally:
        total = test_passed + test_failed
        print(f"\nSummary: ✅ {test_passed} passed, ❌ {test_failed} failed (total {total})")


if __name__ == "__main__":
    asyncio.run(main())