# Generated by Django 4.1.4 on 2023-01-10 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0003_alter_userprofile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
    ]
