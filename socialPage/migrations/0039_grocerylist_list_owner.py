# Generated by Django 4.1.4 on 2023-01-24 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialPage', '0038_remove_grocerylist_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocerylist',
            name='list_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
