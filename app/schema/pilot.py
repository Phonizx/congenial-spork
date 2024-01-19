from pydantic import Field

from app.schema.Base import Base, PyObjectId


class CreatePilotOutput(Base):
    inserted_id : PyObjectId = Field(description="inserted db objectId", default_factory=PyObjectId)


class PatchPilot(Base):
    name : str
