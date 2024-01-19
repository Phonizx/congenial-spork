from fastapi import APIRouter

echo_router = APIRouter(
    prefix="/echo",
    tags=["echo"],
    responses={404: {"description": "Not Found"}},
)


@echo_router.get("/")
async def echo():
    return {"echo": "200"}
