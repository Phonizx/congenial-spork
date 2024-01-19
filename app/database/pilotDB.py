from app.database.BaseCrud import CRUDBase
from app.model.pilot import Pilot


class PilotDB(CRUDBase[Pilot]):
    def __init__(self) -> None:
        super().__init__(model=Pilot, collection_name="Pilot")


pilot_db = PilotDB()
