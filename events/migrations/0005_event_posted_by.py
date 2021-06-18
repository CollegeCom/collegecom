# Generated by Django 2.2.24 on 2021-06-18 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210618_1149'),
        ('events', '0004_auto_20210614_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='accounts.extUser'),
        ),
    ]
