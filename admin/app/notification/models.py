import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationSendStatus(models.TextChoices):
    WAITING = 'waiting', _('Waiting')
    PROCESSING = 'processing', _('Processing')
    DONE = 'done', _('Done')


class TimeStampedModel(models.Model):

    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class MessageTag(TimeStampedModel):

    tag = models.CharField(_('Title'), max_length=255)

    def __str__(self):
        return self.tag


class NotificationType(TimeStampedModel):

    title = models.CharField(_('Title'), max_length=255)
    tags = models.ManyToManyField(MessageTag, through='NotificationTypeTag')

    def __str__(self):
        return self.title


class NotificationTypeTag(TimeStampedModel):

    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    tag = models.ForeignKey(MessageTag, on_delete=models.CASCADE)


class Template(TimeStampedModel):

    title = models.CharField(_('Title'), max_length=255)
    subject = models.CharField(_('Subject'), max_length=255)
    code = models.TextField(_("HTML code or Text"), null=False, blank=False, default='')
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class NotificationContext(models.Model):

    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    params = models.JSONField(blank=False, null=False, default=dict)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.template)


class Notification(TimeStampedModel):

    context = models.ForeignKey(NotificationContext, on_delete=models.CASCADE)
    send_status = models.CharField(
        _('Send status'),
        max_length=50,
        choices=NotificationSendStatus.choices,
        default=NotificationSendStatus.WAITING,
    )
    send_date = models.DateTimeField(editable=True, auto_now=True)


class NotificationGroup(TimeStampedModel):

    title = models.CharField(_('Title'), max_length=255)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class NotificationGroupUser(models.Model):

    notification_group = models.ForeignKey(NotificationGroup, on_delete=models.CASCADE)
    user = models.UUIDField()


class NotificationUnsubscribeUser(models.Model):

    user = models.UUIDField()
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
