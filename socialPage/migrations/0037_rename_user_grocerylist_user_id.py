# Generated by Django 4.1.4 on 2023-01-24 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0036_grocerylist_user_alter_grocerylist_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocerylist',
            old_name='user',
            new_name='user_id',
        ),
    ]
