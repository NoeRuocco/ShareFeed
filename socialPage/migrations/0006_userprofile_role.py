# Generated by Django 4.1.4 on 2023-01-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0005_userprofile_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
