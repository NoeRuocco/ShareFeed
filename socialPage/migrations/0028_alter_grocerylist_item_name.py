# Generated by Django 4.1.4 on 2023-01-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0027_alter_singleitem_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='item_name',
            field=models.ManyToManyField(blank=True, related_name='grocery_list', to='socialPage.singleitem'),
        ),
    ]
