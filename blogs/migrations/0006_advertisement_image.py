# Generated by Django 4.2.6 on 2023-11-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, default='adv-default.jpg', null=True, upload_to='advertisements/', verbose_name='Изображение'),
        ),
    ]
