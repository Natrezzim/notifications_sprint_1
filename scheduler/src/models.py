from typing import Optional

from pydantic import BaseModel


class Context(BaseModel):
    users_id: Optional[list]
    group_id: Optional[str]
    payload: dict


class Message(BaseModel):
    type_send: str
    notification_id: str
    template_id: str
    context: Context
