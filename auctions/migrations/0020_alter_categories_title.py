# Generated by Django 4.0.4 on 2022-08-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_listings_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
