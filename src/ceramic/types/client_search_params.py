# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientSearchParams", "Params"]


class ClientSearchParams(TypedDict, total=False):
    id: Required[int]
    """A unique identifier for the request."""

    jsonrpc: Required[Literal["2.0"]]
    """JSON-RPC version. Must be "2.0"."""

    method: Required[Literal["query"]]
    """The method to call. Use "query" for search."""

    params: Required[Params]


class Params(TypedDict, total=False):
    query: Required[str]
    """The search query in natural language."""

    max_description_length: Annotated[int, PropertyInfo(alias="maxDescriptionLength")]
    """Maximum character length for result descriptions."""

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
    """Maximum number of results to return."""
