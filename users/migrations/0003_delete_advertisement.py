# Generated by Django 4.2.6 on 2023-11-10 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_profile_profiles_advertisement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advertisement',
        ),
    ]
