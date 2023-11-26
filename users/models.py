from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    short_info = models.CharField(max_length=300, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True,
                                      default='profiles/user-default.png')
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_vk = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(Profiles, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='отправитель')
    recipient = models.ForeignKey(Profiles, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='messages', verbose_name='получатель')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='имя отправителя')
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True, verbose_name='тема письма')
    body = models.TextField(verbose_name='текст письма')
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']
