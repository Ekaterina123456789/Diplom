# Generated by Django 4.2.6 on 2023-10-29 20:27

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('contacts', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='video_link',
            new_name='source_link',
        ),
        migrations.AddField(
            model_name='blog',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, verbose_name='Видео'),
        ),
    ]
