from turtle import title
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listings, Bids, Comments, Categories


def checkwatchlist(request, listing_id):
    if request.user.is_authenticated:
        for watch in request.user.wishlist.all():
            if (watch.id == listing_id):
                return True
            else:
                return False
    return False


def index(request):
    Listing = Listings.objects.all()
    return render(request, "auctions/index.html", {
        "listings": Listing
    })


def category(request, category_id):
    Category = Categories.objects.get(id=category_id)
    Listing = Listings.objects.filter(category=Category)
    return render(request, "auctions/index.html", {
        "listings": Listing
    })


def categories(request):
    categories = Categories.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })


def watchlist(request):
    if request.user.is_authenticated:
        Listing = request.user.wishlist.all()
        return render(request, "auctions/watchlist.html", {
            "listings": Listing
        })
    else:
        return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createlisting(request):
    if request.method == "POST":
        # Creating a new listing
        Title = request.POST["Title"]
        Category = request.POST["category"]
        if Category == "Select the Categories":
            return render(request, "auctions/createlisting.html", {
                "categories": Categories.objects.all(),
                "message": "Please select a category",
            })
        Image_url = request.POST["image_url"]
        Description = request.POST["description"]
        Desired_price = request.POST["desired_price"]
        User_obj = request.user
        User = User_obj.username
        listing = Listings(title=Title, image_url=Image_url,
                           description=Description, desired_price=Desired_price, highest_bid=Desired_price, users=User)
        listing.save()
        bid = Bids(user=User, listing_id=listing.id, bid_price=Desired_price)
        bid.save()
        listing.bid = bid
        category_obj = Categories.objects.get(title=Category)
        listing.category = category_obj
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/createlisting.html", {
            "categories": Categories.objects.all(),
        })


def listing(request, listing_id):
    try:
        listing_obj = Listings.objects.get(id=listing_id)
    except Listings.DoesNotExist:
        return render(request, "auctions/listing.html", {
            "message": "This listing does not exist"
        })
    return render(request, "auctions/listing.html", {
        "listing": listing_obj,
        "comments": Comments.objects.all().order_by('-id'),
        "addedtowatchlist": checkwatchlist(request, listing_id)
    })


def createbid(request, listing_id):
    try:
        listing_obj = Listings.objects.get(id=listing_id)
    except Listings.DoesNotExist:
        return render(request, "auctions/listing.html", {
            "message": "This listing does not exist"
        })
    if request.user.is_authenticated:
        if request.method == "POST":
            if int(request.POST["Bid_Price"]) > listing_obj.highest_bid:
                # Creating a new bid
                price = request.POST["Bid_Price"]
                User = request.user
                username = User.username
                bid = Bids(user=username, listing_id=listing_id,
                           bid_price=price)
                bid.save()
                if (listing_obj.highest_bid < int(price)):
                    listing_obj.highest_bid = bid.bid_price
                    listing_obj.bid = bid
                    listing_obj.save()
                return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))
            else:
                return render(request, "auctions/listing.html", {
                    "listing": listing_obj,
                    "comments": Comments.objects.all().order_by('-id'),
                    "bid_message": "Bid should be greater than the highest bid",
                    "addedtowatchlist": checkwatchlist(request, listing_id)
                })
        else:
            return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_obj,
            "comments": Comments.objects.all().order_by('-id'),
            "bid_message": "Please log in first",
            "addedtowatchlist": checkwatchlist(request, listing_id)
        })


def comment(request, listing_id):
    try:
        listing_obj = Listings.objects.get(id=listing_id)
    except Listings.DoesNotExist:
        return render(request, "auctions/listing.html", {
            "message": "This listing does not exist"
        })
    if request.user.is_authenticated:
        if request.method == "POST":
            # Creating a new bid
            comment = request.POST["comment"]
            User = request.user
            username = User.username
            Comment = Comments(
                user=username, listing=listing_id, comment=comment)
            Comment.save()
            return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))
        else:
            return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_obj,
            "comments": Comments.objects.all().order_by('-id'),
            "comment_message": "Please log in first",
            "addedtowatchlist": checkwatchlist(request, listing_id)
        })


def closelisting(request, listing_id):
    try:
        listing_obj = Listings.objects.get(id=listing_id)
    except Listings.DoesNotExist:
        return render(request, "auctions/listing.html", {
            "message": "This listing does not exist"
        })
    if request.user.username == listing_obj.users:
        listing_obj.active = False
        listing_obj.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))


def addtowishlist(request, listing_id):
    try:
        listing_obj = Listings.objects.get(id=listing_id)
    except Listings.DoesNotExist:
        return render(request, "auctions/listing.html", {
            "message": "This listing does not exist"
        })
    if request.user.is_authenticated:
        if listing_obj.users != request.user.username:
            request.user.wishlist.add(listing_obj)
            request.user.save()
        return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_obj,
            "comments": Comments.objects.all().order_by('-id'),
            "wishlist_message": "Please log in first",
            "addedtowatchlist": checkwatchlist(request, listing_id)
        })


def removefromwatchlist(request, listing_id):
    try:
        listing_obj = Listings.objects.get(id=listing_id)
    except Listings.DoesNotExist:
        return render(request, "auctions/listing.html", {
            "message": "This listing does not exist"
        })
    if request.user.is_authenticated:
        if listing_obj.users != request.user.username:
            request.user.wishlist.remove(listing_obj)
            request.user.save()
        return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_obj,
            "comments": Comments.objects.all().order_by('-id'),
            "wishlist_message": "Please log in first",
            "addedtowatchlist": checkwatchlist(request, listing_id)
        })
