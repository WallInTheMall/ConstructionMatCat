from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Mouse section!")

def white_mouse(request):
    return HttpResponse("white lab one")

def black_mouse(request):
    return HttpResponse("black plagie mouse")

def mices_destiny(request):
    return HttpResponse("One to kill a millions. One to save a lot more")