# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from notifications.models import LikeNotification
# from .models import Like


# @receiver(post_save, sender = Like)
# def post_save_like(sender, instance, created, *args, **kwargs):
#     like_notif = LikeNotification(source = user, destination = tweet.user, tweet = tweet)
#     like_notif.content = f'{like_notif.source} liked your tweet.'
#     like_notif.save()
