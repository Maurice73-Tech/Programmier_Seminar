# Generated by Django 3.2.9 on 2021-12-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0026_auto_20211213_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neuebenutzer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]