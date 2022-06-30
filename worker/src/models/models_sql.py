from sqlalchemy import Column, DateTime, String, Text, text, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


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
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'),
                                  nullable=False, index=True)

    notification_type = relationship('TypeNotification')


class NotificationTypeTag(Base):
    __tablename__ = 'notification_notificationtypetag'

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'),
                                  nullable=False, index=True)
    tag_id = Column(ForeignKey('notification_messagetag.id', deferrable=True, initially='DEFERRED'), nullable=False,
                    index=True)

    notification_type = relationship('TypeNotification')
    tag = relationship('MessageTag')


class UnsubscribeUser(Base):
    __tablename__ = 'notification_notificationunsubscribeuser'
    __table_args__ = {'extend_existing': True}

    id = Column(BigInteger, primary_key=True,
                server_default=text("nextval('notification_notificationunsubscribeuser_id_seq'::regclass)"))
    user_id = Column(UUID, nullable=False)
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'),
                                  nullable=False, index=True)

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
    notification_type_id = Column(ForeignKey('notification_notificationtype.id', deferrable=True, initially='DEFERRED'),
                                  nullable=False, index=True)

    notification_type = relationship('TypeNotification')


class Context(Base):
    __tablename__ = 'notification_notificationcontext'

    id = Column(Text, primary_key=True, index=True)
    params = Column(JSONB(astext_type=Text()), nullable=False)
    template_id = Column(ForeignKey('notification_template.id', deferrable=True, initially='DEFERRED'), nullable=False,
                         index=True)

    template = relationship('Template')


class GroupNotificationUser(Base):
    __tablename__ = 'notification_notificationgroupuser'

    id = Column(BigInteger, primary_key=True,
                server_default=text("nextval('notification_notificationgroupuser_id_seq'::regclass)"))
    user_id = Column(UUID, nullable=False)
    notification_group_id = Column(
        ForeignKey('notification_notificationgroup.id', deferrable=True, initially='DEFERRED'), nullable=False,
        index=True)

    notification_group = relationship('GroupNotification')


class Notification(Base):
    __tablename__ = 'notification_notification'

    id = Column(Text, primary_key=True, index=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
    send_status = Column(String(50), nullable=False)
    send_date = Column(DateTime(True), nullable=False)
    context_id = Column(ForeignKey('notification_notificationcontext.id', deferrable=True, initially='DEFERRED'),
                        nullable=False, index=True)

    context = relationship('Context')
