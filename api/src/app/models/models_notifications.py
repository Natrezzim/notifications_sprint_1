from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic.main import BaseModel


class TypeEnum(str, Enum):
    new_series = 'new_series'
    email_confirmation = 'email_confirmation'
    recommendations = 'recommendations'


class TemplateEnum(str, Enum):
    UUID_1 = "1e6226fb-bc02-4f03-8eef-e8e404d3cf80"
    UUID_2 = "71445491-e8d1-4cde-b8c8-40d0ac57a27a"
    UUID_3 = "6b245076-a36c-4ca2-a419-afa73d70e4fb"


class FilmsData(BaseModel):
    film_id: UUID
    film_name: str


class Payload(BaseModel):
    films_data: Optional[List[FilmsData]]


class Context(BaseModel):
    users_id: Optional[List[UUID]]
    group_id: Optional[UUID]
    payload: Optional[Payload]
    link: Optional[str]


class NotificationsExt(BaseModel):
    type_send: TypeEnum = TypeEnum.new_series
    template_id: TemplateEnum = TemplateEnum.UUID_3
    context: Context
