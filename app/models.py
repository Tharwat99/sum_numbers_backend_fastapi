from pydantic import BaseModel, Field
from typing import Optional


class SumRequest(BaseModel):
    upto: int = Field(..., gt=0, description="Positive integer to sum up to")


class SumResponse(BaseModel):
    success: bool
    value: Optional[int] = None
    error: Optional[str] = None
