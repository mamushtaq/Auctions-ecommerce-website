from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:category_id>", views.category, name="category"),
    path("categories", views.categories, name="categories"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting",
         views.createlisting, name="createlisting"),
    path("<int:listing_id>/listing", views.listing, name="listing"),
    path("<int:listing_id>/createbid", views.createbid, name="createbid"),
    path("<int:listing_id>/comment", views.comment, name="comment"),
    path("<int:listing_id>/closelisting",
         views.closelisting, name="closelisting"),
    path("<int:listing_id>/addtowishlist",
         views.addtowishlist, name="addtowishlist"),
    path("<int:listing_id>/removefromwatchlist",
         views.removefromwatchlist, name="removefromwatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
]
