# Generated by Django 4.1.4 on 2023-01-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0041_alter_grocerylist_grocery_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='grocery_items',
            field=models.ManyToManyField(blank=True, related_name='grocery_items', to='socialPage.singleitem'),
        ),
    ]
