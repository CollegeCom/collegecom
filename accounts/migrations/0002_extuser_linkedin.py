# Generated by Django 3.1.7 on 2021-06-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
