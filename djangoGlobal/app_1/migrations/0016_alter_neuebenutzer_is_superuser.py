# Generated by Django 3.2.9 on 2021-11-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0015_alter_neuebenutzer_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neuebenutzer',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
