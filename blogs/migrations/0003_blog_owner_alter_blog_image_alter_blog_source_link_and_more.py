# Generated by Django 4.2.6 on 2023-11-07 10:46

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('blogs', '0002_advertisement_rename_video_link_blog_source_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='blogs/%Y/%m', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='source_link',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Ссылка на источник'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blogs.tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, verbose_name='Ссылка на видео'),
        ),
    ]
