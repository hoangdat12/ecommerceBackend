# Generated by Django 4.1 on 2022-08-14 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category_alter_profile_location_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageurl',
            field=models.ImageField(default='images/placeholder.png', upload_to=''),
        ),
    ]
