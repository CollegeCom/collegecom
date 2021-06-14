# Generated by Django 3.2.4 on 2021-06-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('descripton', models.CharField(max_length=1000)),
                ('poster', models.ImageField(upload_to='poster/')),
            ],
        ),
    ]
