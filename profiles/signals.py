from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from datetime import datetime
from .models import Profile


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user = instance, slug = instance.get_username())

@receiver(signal = post_save, sender = Profile)
def post_save_profie(sender, instance, created, *args, **kwargs):
    if created:
        instance.following.add(instance.user)
        instance.slug = instance.user.get_username()
        instance.save()
