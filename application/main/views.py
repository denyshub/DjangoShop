from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  context: dict[str, str] = {
    'title': 'Home',
    'content' : 'Головна сторінка магазину - HOME',
  }

  return render(request, 'main/index.html', context)

def about(request):
  context: dict[str, str] = {
    'title': 'About',
    'content' : 'Сторінка про магазин',
    'text_on_page': 'Текст про те чому ви маєте обрати саме наш магазин.'
  }

  return render(request, 'main/about.html', context)