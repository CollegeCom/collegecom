# Generated by Django 2.2.24 on 2021-06-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='event-list'),
        ),
    ]
