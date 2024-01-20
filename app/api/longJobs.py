from fastapi import APIRouter

jobs_router = APIRouter(
    prefix="/long-jobs",
    tags=["pilot"],
    responses={404: {"description": "Not Found"}},
)
