# Generated by Django 3.2.9 on 2021-12-13 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0032_alter_neuebenutzer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neuebenutzer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profilbilder/'),
        ),
    ]
