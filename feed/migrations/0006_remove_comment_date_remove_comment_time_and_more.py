# Generated by Django 4.2.8 on 2023-12-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20210616_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='date_time',
        ),
        migrations.AddField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='published_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]