from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]
data_db = [

    {'id': 1, 'title': 'Apex legends', 'content':
        '''<h1> Apex legends </h1> вышла 4 февраля 2019 года,
    разработана студией Respawn Entertaiment и издана EA,
    Apex legends это батл роль и жинру шутре от первого лица.
    Платформы: PlayStation 5, PlayStation 4, Nintendo Switch, 
    Windows, GeForce Now, Xbox Series X|S, Xbox One, Android, iOS.
    Игра поддерживется до сихпор и новые обновления выходят раз в 2-3 месяца.
    ''', 'is_published': True},
    {'id': 2, 'title': 'Call of Duty Modern Warfare 3', 'content':
        'Обзор Call of Duty Modern Warfare 3', 'is_published': False},
    {'id': 3, 'title': 'Deep rock galactic', 'content':
        'Обзор Deep rock galactic', 'is_published': True},
]
cats_db = [
    {'id': 1, 'name': 'Шутеры от 1 лица'},
    {'id': 2, 'name': 'Шутеры от 3 лица'},
    {'id': 3, 'name': 'ActionRPG'},
]


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'index.html', context=data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id ={post_id}")


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'index.html', context=data)


# Create your views here.
def categories(request, genre_id):
    return HttpResponse(f"<h1>Статьи покатегориям</h1><p >id:{genre_id}</p>")


def categories_by_slug(request, genre_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи покатегориям </h1> <p > slug: {genre_slug} </p> ")


def archive(request, year):
    if year > 2024:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p> {year} </p > ")


def about(request):
    return render(request, 'about.html', {'title': 'О сайте', 'menu': menu})
