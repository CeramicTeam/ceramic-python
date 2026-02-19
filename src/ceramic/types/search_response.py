# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchResponse", "Result", "ResultResult", "ResultSearchMetadata"]


class ResultResult(BaseModel):
    description: str
    """A text snippet from the page content."""

    score: float
    """Relevance score for the result."""

    title: str
    """The title of the web page."""

    url: str
    """The URL of the web page."""


class ResultSearchMetadata(BaseModel):
    execution_time: float = FieldInfo(alias="executionTime")
    """Time taken to execute the search in seconds."""


class Result(BaseModel):
    results: List[ResultResult]
    """Array of search results."""

    search_metadata: ResultSearchMetadata = FieldInfo(alias="searchMetadata")

    total_results: int = FieldInfo(alias="totalResults")
    """Total number of results returned."""


class SearchResponse(BaseModel):
    request_id: str = FieldInfo(alias="requestId")
    """Server-generated request identifier (often a UUID)."""

    result: Result
