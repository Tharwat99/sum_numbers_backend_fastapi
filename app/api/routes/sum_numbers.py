from fastapi import APIRouter

from models import SumRequest, SumResponse

router = APIRouter(prefix="", tags=["sum_numbers"])


@router.post("/sum", response_model=SumResponse)
def calculate_sum(request: SumRequest):
    """
    Calculate the sum of all numbers from 1 to the given number.

    Args:
        request (SumRequest): A SumRequest object containing the number upto which the sum needs to be calculated.

    Returns:
        SumResponse: A SumResponse object containing the total sum and/or an error message.
    """
    try:
        total = request.upto * (request.upto + 1) // 2
        
        return SumResponse(
            success=True,
            value=total,
            error=None
        )
    except Exception as e:
        return SumResponse(
            success=False,
            value=None,
            error=str(e)
        )