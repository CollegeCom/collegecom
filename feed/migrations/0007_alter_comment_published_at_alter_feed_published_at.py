# Generated by Django 4.2.8 on 2023-12-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_remove_comment_date_remove_comment_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='published_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
