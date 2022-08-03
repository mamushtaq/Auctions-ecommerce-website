from ast import Num
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from torch import matrix_rank


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    wishlist = models.ManyToManyField('Listings')
    pass


class Bids(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=64)
    listing_id = models.IntegerField(null=True, default=0)
    bid_price = models.IntegerField(null=True, default=0)


class Listings(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    desired_price = models.IntegerField(null=True, default=0)
    users = models.CharField(max_length=64)
    highest_bid = models.IntegerField(null=True, default=0)
    active = models.BooleanField(default=True)
    bid = models.OneToOneField(
        Bids, on_delete=models.CASCADE, primary_key=False, null=True)
    category = models.OneToOneField(
        'Categories', on_delete=models.CASCADE, primary_key=False, null=True)


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    user = models.CharField(max_length=64)
    listing = models.IntegerField(null=True, default=0)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
