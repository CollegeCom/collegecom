# Generated by Django 2.2.1 on 2021-06-16 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=10000)),
                ('date_time', models.CharField(max_length=50)),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='feed_images/')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]