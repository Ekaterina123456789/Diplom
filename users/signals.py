from .models import Profiles, User
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=User)
def profile_update(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profiles.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


@receiver(post_save, sender=Profiles)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created is False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profiles)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
