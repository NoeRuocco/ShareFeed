# Generated by Django 4.1.4 on 2023-01-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPage', '0011_image_remove_post_image_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
    ]
