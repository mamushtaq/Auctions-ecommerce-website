# Generated by Django 4.0.4 on 2022-08-03 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listings_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='bid',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='auctions.bids'),
            preserve_default=False,
        ),
    ]