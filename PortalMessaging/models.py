from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Message(models.Model):
    time_send = models.DateTimeField(_('Time send'), auto_now_add=True)
    time_read = models.DateTimeField(_('Time read'), blank=True, null=True)
    reply = models.ForeignKey('self', related_name='parent', blank=True, null=True)
    sender = models.ForeignKey(User, related_name='Sender')
    receiver = models.ForeignKey(User, related_name='Receiver')
    topic = models.CharField(_('Topic'), max_length=64)
    message = models.TextField(_('Message'))

    def __str__(self):
        return "Sender [%s] - [%s] - %s" % (self.sender.username, self.receiver.username, self.topic)


