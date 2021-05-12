# Generated by Django 3.2 on 2021-05-10 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_blogpost_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='text',
            new_name='body',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='displayText',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]