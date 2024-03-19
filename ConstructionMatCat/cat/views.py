from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Cool")

def cats(request):
    return HttpResponse("Котики")

def orange_cat(request):
    return HttpResponse("Рыжий котик")


def black_cat(request):
    return HttpResponse("Чёрный котик")


def white_cat(request):
    return HttpResponse("Белый котик")