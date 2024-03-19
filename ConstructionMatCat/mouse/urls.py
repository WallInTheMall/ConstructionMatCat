from . import views
from django.urls import path, include

micepatterns = [
    path("white", views.white_mouse, name="whitemouse"),
    path("black", views.black_mouse, name="blackmouse"),
    path("white", views.mices_destiny, name="destiny")
]

urlpatterns = [
    path("", views.index, name="index"),
    path("", include(micepatterns))
]
