from typing import Annotated, Any, Callable

from bson import ObjectId
from pydantic import BaseModel
from pydantic_core import core_schema

# thanks to https://stackoverflow.com/questions/76686888/using-bson-objectid-in-pydantic-v2/76837550#76837550,
# https://www.mongodb.com/community/forums/t/pydantic-v2-and-objectid-fields/241965/4


class _ObjectIdPydanticAnnotation:
    # Based on https://docs.pydantic.dev/latest/usage/types/custom/#handling-third-party-types.

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        def validate_from_str(input_value: str) -> ObjectId:
            return ObjectId(input_value)

        return core_schema.union_schema(
            [
                # check if it's an instance first before doing any further work
                core_schema.is_instance_schema(ObjectId),
                core_schema.no_info_plain_validator_function(validate_from_str),
            ],
            serialization=core_schema.to_string_ser_schema(),
        )


PyObjectId = Annotated[
    ObjectId, _ObjectIdPydanticAnnotation
]


class Base(BaseModel):
    """Base Schema model"""

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
