# Generated by Django 4.1.4 on 2023-01-18 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0014_remove_post_images_delete_image_post_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, choices=[('Meat or Fish', 'meat or fish'), ('Frozen goods', 'frozen goods'), ('Canned food', 'canned food'), ('Fruits', 'fruits'), ('Vegetables', 'vegetables'), ('Nuts', 'nuts'), ('Eggs', 'eggs'), ('Pasta', 'pasta'), ('Bread', 'bread'), ('Salty snacks', 'salty snacks'), ('Sweet snacks', 'sweet snacks'), ('Pastry', 'pastry'), ('Water or Soft drinks', 'water or soft drinks'), ('Energy drinks', 'energy drinks'), ('Alcoholic drinks', 'alcoholic drinks'), ('Coffee or Tea', 'coffee or tea'), ('Spices', 'spices'), ('Seasoning', 'seasoning')], max_length=50, null=True)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, choices=[('Ristoratore', 'ristoratore'), ('Cuoco amatoriale', 'cuoco amatoriale')], max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='CategoryStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage_method', models.CharField(blank=True, choices=[('Pantry', 'pantry'), ('Fridge', 'fridge'), ('Freezer', 'freezer'), ('Other', 'other')], max_length=30, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialPage.grocery_list')),
            ],
        ),
    ]
