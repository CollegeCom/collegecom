# Generated by Django 2.1.15 on 2021-06-12 18:45

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
            name='extUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('enroll', models.CharField(blank=True, max_length=255, null=True)),
                ('sem', models.IntegerField(default=1)),
                ('branch', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('institution', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
