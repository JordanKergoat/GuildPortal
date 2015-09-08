from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class Message(models.Model):
    time_send = models.DateTimeField(_('Time send'), auto_now_add=True)
    time_read = models.DateTimeField(_('Time read'), blank=True, null=True)
    read = models.BooleanField(default=False)
    reply = models.ForeignKey('self', related_name='parent', blank=True, null=True)
    sender = models.ForeignKey(User, related_name='Sender')
    receiver = models.ForeignKey(User, related_name='Receiver')
    topic = models.CharField(_('Topic'), max_length=64)
    message = models.TextField(_('Message'))



