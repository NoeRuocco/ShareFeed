# Generated by Django 4.1.4 on 2023-01-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0025_alter_grocerylist_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleitem',
            name='item_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Model name'),
        ),
    ]