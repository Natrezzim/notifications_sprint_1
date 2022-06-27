from datetime import datetime
import enum
from uuid import UUID

from sqlalchemy import Enum, TIMESTAMP
from sqlmodel import SQLModel, Field, Column


class StatusEnum(str, enum.Enum):
    waiting = 'waiting'
    processing = 'processing'
    done = 'done'


class NotificationBase(SQLModel):
    id: UUID
    context_id: UUID
    send_status: StatusEnum
    send_date: datetime
    created: datetime
    updated: datetime


class Notification(NotificationBase, table=True):
    id: UUID = Field(default=None, primary_key=True)
    send_status: StatusEnum = Field(sa_column=Column(Enum(StatusEnum)))
    send_date: datetime = Field(sa_column=Column(type_=TIMESTAMP(timezone=True)))
    created: datetime = Field(sa_column=Column(type_=TIMESTAMP(timezone=True)))
    updated: datetime = Field(sa_column=Column(type_=TIMESTAMP(timezone=True)))


class NotificationCreate(NotificationBase):
    pass


class ContextBase(SQLModel):
    id: UUID
    params: str
    tamplate_id: UUID


class Context(NotificationBase, table=True):
    id: UUID = Field(default=None, primary_key=True)


class TemplateBase(SQLModel):
    id: UUID
    title: str
    subject: str
    code: str
    type: str


class Template(NotificationBase, table=True):
    id: UUID = Field(default=None, primary_key=True)
