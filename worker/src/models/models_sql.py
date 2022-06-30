# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, JSON, String, Text, text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Notification(Base):
    __tablename__ = 'notification'
    id = Column(UUID, nullable=False, unique=True, primary_key=True)
    context_id = Column(ForeignKey("context.id"), nullable=False)
    send_status = Column(Enum('waiting', 'processing', 'done', name='send_status'), nullable=False,
                         server_default=text("'waiting'::send_status"))
    send_date = Column(DateTime, nullable=False, server_default=text("CURRENT_DATE"))
    created = Column(DateTime, nullable=False, server_default=text("CURRENT_DATE"))
    updated = Column(DateTime)


class TypeNotification(Base):
    __tablename__ = 'type_notification'
    id = Column(UUID, nullable=False, unique=True, primary_key=True)
    title = Column(String(255), nullable=False)


class Context(Base):
    __tablename__ = 'context'
    id = Column(UUID, nullable=False, unique=True, primary_key=True)
    params = Column(JSON, nullable=False)
    template_id = Column(ForeignKey("template.id"), nullable=False)


class GroupNotification(Base):
    __tablename__ = 'group_notification'
    id = Column(UUID, nullable=False, unique=True, primary_key=True)
    title = Column(String(255), nullable=False)
    type_notification_id = Column(ForeignKey("type_notification.id"), nullable=False)


class GroupNotificationUser(Base):
    __tablename__ = 'group_notification_user'
    id = Column(UUID, primary_key=True)
    group_notification_id = Column(ForeignKey("group_notification.id"), nullable=False)
    user_id = Column(UUID, nullable=False)


class Template(Base):
    __tablename__ = 'template'
    id = Column(UUID, nullable=False, unique=True, primary_key=True)
    title = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    code = Column(Text, nullable=False)
    type_notification_id = Column(ForeignKey("type_notification.id"), nullable=False)


class UnsubscribeUser(Base):
    __tablename__ = 'unsubscribe_user'
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, nullable=False)
    type_notification_id = Column(ForeignKey("type_notification.id"), nullable=False)
