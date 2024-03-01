from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": 'Главная страница',
        "content": 'Магазин цветов',
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": 'О нас',
        "content": 'Инфа обо мне и магазе',
        "text_page": "Ваще крутой магаз, покупай 100 цветов",
    }
    return render(request, "about.html", context)
