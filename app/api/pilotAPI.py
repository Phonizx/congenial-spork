from bson import ObjectId
from fastapi import APIRouter, Response, status

from app.middleware import create_pilot, delete_pilot, read_pilot, update_pilot
from app.model.pilot import Pilot
from app.schema.pilot import CreatePilotOutput, PatchPilot

pilot_router = APIRouter(
    prefix="/pilot",
    tags=["pilot"],
    responses={404: {"description": "Not Found"}},
)


@pilot_router.post("/", response_model=CreatePilotOutput)
async def create_pilot_view(pilot : Pilot) -> CreatePilotOutput:
    inserted_pilot_id = await create_pilot(pilot=pilot)
    return CreatePilotOutput(inserted_id=inserted_pilot_id)


@pilot_router.get("/{id}", response_model=Pilot)
async def read_pilot_view(id : str) -> Pilot | Response:
    pilot : Pilot = await read_pilot(object_id=ObjectId(id))
    if not pilot:
        return Response(content="Pilot not found.", status_code=status.HTTP_404_NOT_FOUND)
    return pilot


@pilot_router.patch("/{id}", response_model=Pilot)
async def patch_pilot_view(id : str, updated_pilot : PatchPilot) -> Pilot | Response:
    pilot : Pilot = await update_pilot(object_id=ObjectId(id), pilot_update=updated_pilot)
    if not pilot:
        return Response(content="Pilot not found.", status_code=status.HTTP_404_NOT_FOUND)
    return pilot


@pilot_router.delete("/{id}", response_model=Pilot)
async def delete_pilot_view(id : str) -> Response:
    await delete_pilot(object_id=ObjectId(id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
