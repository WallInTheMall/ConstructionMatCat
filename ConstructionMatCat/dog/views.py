from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Собачки")

def sobaka_one(request):
    return HttpResponse("Лабрадор")

def sobaka_two(request):
    return HttpResponse("Овчарка")