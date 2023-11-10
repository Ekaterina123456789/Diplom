from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    short_info = models.CharField(max_length=300, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(max_length=200, null=True, blank=True)
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


class Advertisement(models.Model):
    text = models.TextField(null=True, blank=True)
    contacts = models.CharField(max_length=250)
    owner = models.ForeignKey(Profiles, on_delete=models.SET_NULL,
                              blank=True, null=True, verbose_name='Автор объявления')

    def __str__(self):
        return self.text

