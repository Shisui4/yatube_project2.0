from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница записулек')


def group_posts(request, slug):
    return HttpResponse(f'Страница с {slug}')
