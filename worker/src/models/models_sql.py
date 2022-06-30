# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, JSON, String, Text, text, ForeignKey, BigInteger, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
#
# class Notification(Base):
#     __tablename__ = 'notification_notification'
#
#     id = Column(Text, primary_key=True, index=True)
#     created_at = Column(DateTime(True))
#     updated_at = Column(DateTime(True))
#     send_status = Column(Enum('waiting', 'processing', 'done', name='send_status'), nullable=False,
#                          server_default=text("'waiting'::send_status"))
#     send_date = Column(DateTime(True), nullable=False)
#     context_id = Column(ForeignKey('Context.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
#
#     context = relationship('Context')

#
# class Notification(Base):
#     __tablename__ = 'notification'
#     id = Column(UUID, nullable=False, unique=True, primary_key=True)
#     context_id = Column(ForeignKey("context.id"), nullable=False)
#     send_status = Column(Enum('waiting', 'processing', 'done', name='send_status'), nullable=False,
#                          server_default=text("'waiting'::send_status"))
#     send_date = Column(DateTime, nullable=False, server_default=text("CURRENT_DATE"))
#     created = Column(DateTime, nullable=False, server_default=text("CURRENT_DATE"))
#     updated = Column(DateTime)


# class TypeNotification(Base):
#     __tablename__ = 'type_notification'
#     id = Column(UUID, nullable=False, unique=True, primary_key=True)
#     title = Column(String(255), nullable=False)

# class TypeNotification(Base):
#     __tablename__ = 'notification_notificationtype'
#
#     id = Column(Text, primary_key=True, index=True)
#     created_at = Column(DateTime(True))
#     updated_at = Column(DateTime(True))
#     title = Column(String(255), nullable=False)
#


# class Context(Base):
#     __tablename__ = 'notification_notificationcontext'
#
#     id = Column(Text, primary_key=True, index=True)
#     params = Column(JSONB, nullable=False)
#     template_id = Column(ForeignKey('Template.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
#
#     template = relationship('Template')

# class Context(Base):
#     __tablename__ = 'context'
#     id = Column(UUID, nullable=False, unique=True, primary_key=True)
#     params = Column(JSON, nullable=False)
#     template_id = Column(ForeignKey("template.id"), nullable=False)


# class GroupNotification(Base):
#     __tablename__ = 'group_notification'
#     id = Column(UUID, nullable=False, unique=True, primary_key=True)
#     title = Column(String(255), nullable=False)
#     type_notification_id = Column(ForeignKey("type_notification.id"), nullable=False)
#

# class GroupNotification(Base):
#     __tablename__ = 'notification_notificationgroup'
#
#     id = Column(Text, primary_key=True, index=True)
#     created_at = Column(DateTime(True))
#     updated_at = Column(DateTime(True))
#     title = Column(String(255), nullable=False)
#     notification_type_id = Column(ForeignKey('TypeNotification.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
#
#     notification_type = relationship('TypeNotification')

#
# class GroupNotificationUser(Base):
#     __tablename__ = 'group_notification_user'
#     id = Column(UUID, primary_key=True)
#     group_notification_id = Column(ForeignKey("group_notification.id"), nullable=False)
#     user_id = Column(UUID, nullable=False)

# class GroupNotificationUser(Base):
#     __tablename__ = 'notification_notificationgroupuser'
#
#     id = Column(BigInteger, primary_key=True)
#     user = Column(UUID, nullable=False)
#     notification_group_id = Column(ForeignKey('GroupNotification.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
#
#     notification_group = relationship('GroupNotification')
#


# class Template(Base):
#     __tablename__ = 'template'
#     id = Column(UUID, nullable=False, unique=True, primary_key=True)
#     title = Column(String(255), nullable=False)
#     subject = Column(String(255), nullable=False)
#     code = Column(Text, nullable=False)
#     type_notification_id = Column(ForeignKey("type_notification.id"), nullable=False)
#

# class Template(Base):
#     __tablename__ = 'notification_template'
#
#     id = Column(Text, primary_key=True, index=True)
#     created_at = Column(DateTime(True))
#     updated_at = Column(DateTime(True))
#     title = Column(String(255), nullable=False)
#     subject = Column(String(255), nullable=False)
#     code = Column(Text, nullable=False)
#     notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
#
#     notification_type = relationship('TypeNotification')
#


# class UnsubscribeUser(Base):
#     __tablename__ = 'unsubscribe_user'
#     id = Column(UUID, primary_key=True)
#     user_id = Column(UUID, nullable=False)
#     type_notification_id = Column(ForeignKey("type_notification.id"), nullable=False)
#
# class UnsubscribeUser(Base):
#     __tablename__ = 'notification_notificationunsubscribeuser'
#
#     id = Column(BigInteger, primary_key=True)
#     user = Column(UUID, nullable=False)
#     notification_type_id = Column(ForeignKey('TypeNotification.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
#
#     notification_type = relationship('TypeNotification')
#


class MessageTag(Base):
    __tablename__ = 'notification_messagetag'

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    tag = Column(String(255), nullable=False)


class TypeNotification(Base):
    __tablename__ = 'notification_notificationtype'

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    title = Column(String(255), nullable=False)




class GroupNotification(Base):
    __tablename__ = 'notification_notificationgroup'

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    title = Column(String(255), nullable=False)
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    notification_type = relationship('TypeNotification')


class NotificationTypeTag(Base):
    __tablename__ = 'notification_notificationtypetag'

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    tag_id = Column(ForeignKey('notification_messagetag.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    notification_type = relationship('TypeNotification')
    tag = relationship('MessageTag')


class UnsubscribeUser(Base):
    __tablename__ = 'notification_notificationunsubscribeuser'
    __table_args__ = {'extend_existing': True}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('notification_notificationunsubscribeuser_id_seq'::regclass)"))
    user_id = Column(UUID, nullable=False)
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    notification_type = relationship('TypeNotification')


class Template(Base):
    __tablename__ = 'notification_template'
    __table_args__ = {'extend_existing': True}

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    title = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    code = Column(Text, nullable=False)
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    notification_type = relationship('TypeNotification')

class Context(Base):
    __tablename__ = 'notification_notificationcontext'

    id = Column(Text, primary_key=True, index=True)
    params = Column(JSONB(astext_type=Text()), nullable=False)
    template_id = Column(ForeignKey('notification_template.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    template = relationship('Template')


class GroupNotificationUser(Base):
    __tablename__ = 'notification_notificationgroupuser'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('notification_notificationgroupuser_id_seq'::regclass)"))
    user_id = Column(UUID, nullable=False)
    notification_group_id = Column(ForeignKey('notification_notificationgroup.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    notification_group = relationship('GroupNotification')


class Notification(Base):
    __tablename__ = 'notification_notification'

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    send_status = Column(String(50), nullable=False)
    send_date = Column(DateTime(True), nullable=False)
    context_id = Column(ForeignKey('notification_notificationcontext.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    context = relationship('Context')
