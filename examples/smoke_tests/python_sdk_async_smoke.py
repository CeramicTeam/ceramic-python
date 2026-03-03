import os
import asyncio
from typing import Awaitable, Callable, Iterable, Mapping, Optional, Tuple, Type, cast

from ceramic_ai import AsyncCeramic
from ceramic_ai._exceptions import (
    CeramicError,
    APIStatusError,
    AuthenticationError,
    BadRequestError,
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
        base_url="https://api.ceramic.ai",
    )


# ---------------------------
# 1) Basic query
# ---------------------------

async def ex_basic_query() -> None:
    client = make_client()
    await expect_ok("basic query", lambda: client.search(query="California rental laws"))


# ---------------------------
# 2) Basic query + params
# ---------------------------

async def ex_basic_query_with_params() -> None:
    client = make_client()
    await expect_ok(
        "basic query + max_results/max_description_length",
        lambda: client.search(
            query="Stanford CS229",
            max_results=3,
            max_description_length=200,
        ),
    )


# ---------------------------
# 3) Invalid API key
# ---------------------------

async def ex_invalid_api_key() -> None:
    client = make_client(api_key="invalid_api_key")
    await expect_api_error(
        "invalid api key",
        lambda: client.search(query="test invalid key"),
        status=401,
        code="invalid_api_key",
        exc=AuthenticationError,
    )


# ---------------------------
# 4) max_results validations
# ---------------------------

async def ex_max_results_validations() -> None:
    client = make_client()

    cases: Iterable[Tuple[str, int, bool]] = [
        ("zero", 0, False),
        ("negative", -1, False),
        ("valid_min", 1, True),
        ("valid_default", 10, True),
        ("very_large", 100, False),
    ]

    for name, mr, is_valid in cases:
        label = f"max_results validation: {name} (max_results={mr})"
        if is_valid:
            await expect_ok(label, lambda: client.search(query="rate limits and retries", max_results=mr))
        else:
            await expect_api_error(
                label,
                lambda: client.search(query="rate limits and retries", max_results=mr),
                status=400,
                code="invalid_parameter",
                exc=BadRequestError,
            )


# ---------------------------
# 5) max_description_length validations
# ---------------------------

async def ex_max_description_length_validations() -> None:
    client = make_client()

    cases: Iterable[Tuple[str, int, bool]] = [
        ("zero", 0, False),
        ("small", 40, False),
        ("valid_small", 50, True),
        ("valid_default", 1500, True),
        ("very_large", 6000, False),
    ]

    for name, mdl, is_valid in cases:
        label = f"max_description_length validation: {name} (max_description_length={mdl})"
        if is_valid:
            await expect_ok(label, lambda: client.search(query="rate limits and retries", max_description_length=mdl))
        else:
            await expect_api_error(
                label,
                lambda: client.search(query="rate limits and retries", max_description_length=mdl),
                status=400,
                code="invalid_parameter",
                exc=BadRequestError,
            )


async def main() -> None:
    try:
        await ex_basic_query()
        await ex_basic_query_with_params()
        await ex_invalid_api_key()
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