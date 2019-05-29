from django.db import models
from django.conf import settings
from tweets.models import Tweet


class Notification(models.Model):
    source = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'from_notif')
    destination = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'to_notif')
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        abstract = True
        ordering = ('-created',)


class LikeNotification(Notification):
    content = models.TextField(blank = True)
    tweet = models.ForeignKey(Tweet, on_delete = models.CASCADE, related_name = 'like_notif')
