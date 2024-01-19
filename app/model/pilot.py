from pydantic import BaseModel


class Pilot(BaseModel):
    id : str
    name : str
