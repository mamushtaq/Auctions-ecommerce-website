# Generated by Django 4.0.4 on 2022-08-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_listings_highest_bid_listings_highest_bid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='listing_title',
        ),
        migrations.AddField(
            model_name='bids',
            name='listing_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.RemoveField(
            model_name='bids',
            name='user',
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
