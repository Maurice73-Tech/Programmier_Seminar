# Generated by Django 4.0 on 2021-12-17 09:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0033_alter_neuebenutzer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Inhalt',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
