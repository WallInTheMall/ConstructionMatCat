from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("THis is the main page!!")
# Create your views here.
