from django.urls import path, include

from . import views

cat_patterns = [
    path("", views.cats),
    path("orange", views.orange_cat),
    path("black", views.black_cat),
    path("whit", views.white_cat)
]

urlpatterns = [
    path("", views.index, name="index"),
    path("cats/", include(cat_patterns))
]