from django.urls import path, include
from . import views

doggos = [
    path("one", views.sobaka_one),
    path("two", views.sobaka_two)
]

urlpatterns = [
    path("", views.index),
    path("by_number/", include(doggos))
]