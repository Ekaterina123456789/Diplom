from django.db import models
from embed_video.fields import EmbedVideoField


class Blog(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="blogs/%Y/%m", default='default.jpg')
    video = EmbedVideoField(blank=True, verbose_name='Видео')
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # autor = User

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    text = models.TextField(null=True, blank=True)
    contacts = models.CharField(max_length=250)
    # autor = User

    def __str__(self):
        return self.text
