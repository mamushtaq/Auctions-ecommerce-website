# Generated by Django 4.0.4 on 2022-08-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_comments_listing_comments_listing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
