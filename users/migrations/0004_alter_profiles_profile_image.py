# Generated by Django 4.2.6 on 2023-11-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_advertisement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]