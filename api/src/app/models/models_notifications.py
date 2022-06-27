from typing import List, Dict, ClassVar
from uuid import UUID

from pydantic.main import BaseModel


class NewSeries(BaseModel):
    type_send: ClassVar[str] = 'new_series'
    template_id: ClassVar[int] = 1
    user_id: UUID
    context: Dict[str, List[UUID]]


class EmailConfirmation(BaseModel):
    type_send: ClassVar[str] = 'email_confirmation'
    template_id: ClassVar[int] = 2
    user_id: UUID
    context: Dict[str, str]


class Recommendations(BaseModel):
    type_send: ClassVar[str] = 'recommendations'
    template_id: ClassVar[int] = 3
    group_id: List[UUID]
    context: Dict[str, str]


class Likes(BaseModel):
    type_send: ClassVar[str] = 'likes'
    template_id: ClassVar[int] = 4
    user_id = UUID
    context: Dict[str, str]
