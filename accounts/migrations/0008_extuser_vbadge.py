# Generated by Django 2.2.24 on 2021-06-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_extuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='vbadge',
            field=models.BooleanField(default=False),
        ),
    ]
