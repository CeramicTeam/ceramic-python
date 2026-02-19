# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchResponse", "Result", "ResultResult", "ResultSearchMetadata"]


class ResultResult(BaseModel):
    description: Optional[str] = None
    """A text snippet from the page content."""

    score: Optional[float] = None
    """Relevance score for the result."""

    title: Optional[str] = None
    """The title of the web page."""

    url: Optional[str] = None
    """The URL of the web page."""


class ResultSearchMetadata(BaseModel):
    execution_time: Optional[float] = FieldInfo(alias="executionTime", default=None)
    """Time taken to execute the search in seconds."""


class Result(BaseModel):
    results: Optional[List[ResultResult]] = None
    """Array of search results."""

    search_metadata: Optional[ResultSearchMetadata] = FieldInfo(alias="searchMetadata", default=None)

    total_results: Optional[int] = FieldInfo(alias="totalResults", default=None)
    """Total number of results returned."""


class SearchResponse(BaseModel):
    id: Optional[int] = None
    """The request ID you provided."""

    jsonrpc: Optional[str] = None
    """JSON-RPC version. Always "2.0"."""

    result: Optional[Result] = None
