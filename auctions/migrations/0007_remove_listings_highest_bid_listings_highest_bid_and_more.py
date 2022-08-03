# Generated by Django 4.0.4 on 2022-08-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bids_listing_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='highest_bid',
        ),
        migrations.AddField(
            model_name='listings',
            name='highest_bid',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
