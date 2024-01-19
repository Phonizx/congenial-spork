# mypy: ignore-errors
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

import motor.motor_asyncio
from bson import ObjectId
from settings import settings

ModelType = TypeVar("ModelType")


# ispirated by my friend, @kludex (Mr. Typer <3 ) https://github.com/Kludex/fastapi-microservices/blob/main/users/app/crud/base.py
class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], collection_name) -> None:
        self._model = model
        client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_CONNECTION_STRING)
        self.db = client["pilot-db"]
        self.collection = self.db[collection_name]

    async def create(
        self, obj_in: ModelType
    ) -> ObjectId:
        obj_dict = dict(obj_in)
        result = await self.collection.insert_one(obj_dict)
        return result.inserted_id

    async def get(self, filter_query: Dict[str, Any], *args, **kwargs) -> Optional[ModelType]:
        result = await self.collection.find_one(filter=filter_query)
        if not result:
            return None
        return self._model(**result)

    async def update(
        self,
        filter_query : Dict[str, Any],
        updated_obj: Union[ModelType, Dict[str, Any]],
        *args,
        **kwargs
    ) -> Optional[ModelType]:
        updated_obj = dict(updated_obj)
        result = await self.collection.replace_one(filter=filter_query, replacement=updated_obj)
        if not result:
            return None
        return self._model(**updated_obj)

    async def delete(
        self, filter_query: Dict[str, Any] = None, *args, **kwargs
    ) -> None:
        await self.collection.delete_one(filter=filter_query)

    async def get_multi(
        self, filter_query : Dict[str, Any], offset: int = 0, limit: int = 100, *args, **kwargs
    ) -> List[ModelType]:
        results = await self.collection.find(filter_query).skip(offset).limit(limit=limit)
        return [self._model(**result) for result in results]

    async def pipeline(
        self, pipeline : List[Dict[str, Any]], proxy_model: ModelType = None, *args, **kwargs
    ) -> List[ModelType]:
        results = await self.collection.aggregate(pipeline=pipeline)
        if not proxy_model:
            return results
        return [proxy_model(**result) for result in results]
