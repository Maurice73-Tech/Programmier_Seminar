# Generated by Django 3.2.8 on 2022-01-09 00:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0044_auto_20220108_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='kommentar',
            name='dislikes',
            field=models.ManyToManyField(related_name='kommentar_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='unterkommentar',
            name='dislikes',
            field=models.ManyToManyField(related_name='unterkommentar_dislikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
