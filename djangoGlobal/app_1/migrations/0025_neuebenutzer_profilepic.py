# Generated by Django 3.2.9 on 2021-12-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0024_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='neuebenutzer',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
