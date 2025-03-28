from fastapi import APIRouter

from .routes import sum_numbers

api_router = APIRouter()
api_router.include_router(sum_numbers.router)
