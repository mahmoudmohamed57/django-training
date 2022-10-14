# Generated by Django 4.1.2 on 2022-10-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_approved',
            field=models.BooleanField(default=True, help_text="is approved if the album name shouldn't contain inappropriate expressions"),
        ),
    ]