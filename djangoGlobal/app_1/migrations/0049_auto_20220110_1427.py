# Generated by Django 3.2.9 on 2022-01-10 13:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0048_rename_parent_unterkommentar_├╝berkommentar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='neuebenutzer',
            options={'verbose_name_plural': 'Benutzer'},
        ),
        migrations.AlterField(
            model_name='kommentar',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='kommentar_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='kommentar',
            name='kommentar',
            field=ckeditor.fields.RichTextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kommentar',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='kommentar_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='Inhalt',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unterkommentar',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='unterkommentar_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unterkommentar',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='unterkommentar_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unterkommentar',
            name='unterkommentar',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, null=True),
        ),
    ]
