# Generated by Django 2.2.24 on 2021-06-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_extuser_vbadge'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='department',
            field=models.CharField(default='IIST', max_length=100),
        ),
    ]
