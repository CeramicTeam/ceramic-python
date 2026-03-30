# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientSearchParams"]


class ClientSearchParams(TypedDict, total=False):
    query: Required[str]
    """The search query in natural language.

    Must contain between 1 and 50 words (words are separated by spaces; extra
    whitespace is ignored).
    """

    max_description_length: Annotated[int, PropertyInfo(alias="maxDescriptionLength")]
    """Maximum character length for result descriptions."""

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
    """Maximum number of results to return."""
