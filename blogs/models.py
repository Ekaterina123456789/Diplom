import datetime

from django.db import models
from embed_video.fields import EmbedVideoField
from users.models import Profiles


class Blog(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Автор')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст новости')
    image = models.ImageField(null=True, blank=True, upload_to="blogs/%Y/%m",
                              default='default.jpg', verbose_name='Изображение')
    video = EmbedVideoField(blank=True, verbose_name='Ссылка на видео')
    source_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Ссылка на источник')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Тег')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="advertisements/",
                              default='adv-default.jpg', verbose_name='Изображение')
    contacts = models.CharField(max_length=250)
    owner = models.ForeignKey(Profiles, on_delete=models.SET_NULL,
                              blank=True, null=True, verbose_name='Автор объявления')
    created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['owner', 'blog'], ]
        ordering = ['-created']
