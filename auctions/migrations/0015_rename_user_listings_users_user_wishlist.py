# Generated by Django 4.0.4 on 2022-08-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_listings_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='user',
            new_name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(to='auctions.listings'),
        ),
    ]
