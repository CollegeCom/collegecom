# Generated by Django 2.2.24 on 2021-06-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_extuser_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuser',
            name='profileimg',
            field=models.ImageField(default='profile_images/user.jpeg', upload_to='profile_images/'),
        ),
    ]
