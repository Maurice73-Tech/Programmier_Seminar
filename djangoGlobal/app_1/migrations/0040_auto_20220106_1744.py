# Generated by Django 3.2.8 on 2022-01-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0039_remove_kommentar_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unterkommentar',
            name='post',
        ),
        migrations.AlterField(
            model_name='unterkommentar',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unterkommentar', to='app_1.kommentar'),
        ),
    ]
