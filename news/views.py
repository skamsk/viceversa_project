from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category


# Create your views here.
def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)

def test(request):
    return HttpResponse("<H1>Тестовая страница</H1>")


def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)
