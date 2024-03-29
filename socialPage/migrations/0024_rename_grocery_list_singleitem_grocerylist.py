# Generated by Django 4.1.4 on 2023-01-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0023_alter_grocery_list_food_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grocery_list',
            new_name='SingleItem',
        ),
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.ManyToManyField(blank=True, null=True, related_name='items_name', to='socialPage.singleitem')),
            ],
        ),
    ]
