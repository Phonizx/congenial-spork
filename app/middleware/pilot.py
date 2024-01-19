from bson import ObjectId

from app.database.pilotDB import pilot_db
from app.model.pilot import Pilot


async def create_pilot(pilot : Pilot) -> ObjectId:
    return await pilot_db.create(obj_in=pilot)


async def read_pilot(object_id : ObjectId) -> Pilot:
    return await pilot_db.get(filter_query={"_id": object_id})


async def update_pilot(object_id : ObjectId, pilot_update : Pilot) -> Pilot:
    pilot = await read_pilot(object_id=object_id)
    pilot.__dict__.update(
        pilot_update.model_dump(exclude_none=True)
    )
    return await pilot_db.update(filter_query={"_id": object_id}, updated_obj=pilot)


async def delete_pilot(object_id : ObjectId):
    return await pilot_db.delete(filter_query={"_id": object_id})
