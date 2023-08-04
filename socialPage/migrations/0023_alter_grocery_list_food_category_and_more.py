# Generated by Django 4.1.4 on 2023-01-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0022_grocery_list_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery_list',
            name='food_category',
            field=models.CharField(blank=True, choices=[('Meat or Fish', 'meat or fish'), ('Frozen goods', 'frozen goods'), ('Canned food', 'canned food'), ('Fruits', 'fruits'), ('Vegetables', 'vegetables'), ('Nuts', 'nuts'), ('Eggs', 'eggs'), ('Pasta', 'pasta'), ('Bread', 'bread'), ('Salty snacks', 'salty snacks'), ('Sweet snacks', 'sweet snacks'), ('Pastry', 'pastry'), ('Water or Soft drinks', 'water or soft drinks'), ('Energy drinks', 'energy drinks'), ('Alcoholic drinks', 'alcoholic drinks'), ('Coffee or Tea', 'coffee or tea'), ('Spices', 'spices'), ('Seasoning', 'seasoning')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='grocery_list',
            name='storage_method',
            field=models.CharField(blank=True, choices=[('Pantry', 'pantry'), ('Fridge', 'fridge'), ('Freezer', 'freezer'), ('Other', 'other')], max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
