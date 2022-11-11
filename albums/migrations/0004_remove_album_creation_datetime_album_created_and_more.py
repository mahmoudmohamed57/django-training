# Generated by Django 4.1.2 on 2022-10-13 13:41

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_album_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='creation_datetime',
        ),
        migrations.AddField(
            model_name='album',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='album',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
