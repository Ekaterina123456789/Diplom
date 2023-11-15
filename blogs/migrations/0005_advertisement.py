# Generated by Django 4.2.6 on 2023-11-10 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_advertisement'),
        ('blogs', '0004_delete_advertisement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('contacts', models.CharField(max_length=250)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profiles', verbose_name='Автор объявления')),
            ],
        ),
    ]
