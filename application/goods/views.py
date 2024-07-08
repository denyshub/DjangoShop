from django.shortcuts import render

def catalog(request):
    context: dict[str, str] = {
    'title': 'Catalog',
    'content' : 'Каталог товарів',
  }
    return render(request, 'goods/catalog.html', context)


def product(request):
    context: dict[str, str] = {
    'title': 'Product',
    'content' : 'Сторінка товара',
  }
    return render(request, 'goods/product.html', context)
