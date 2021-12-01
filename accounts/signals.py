from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('hello from user receiver')
    if created:
        Profile.objects.create(user=instance)


