# Generated by Django 4.0.4 on 2022-08-03 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_alter_categories_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.categories'),
        ),
    ]
