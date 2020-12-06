from django import template

from news.models import Category
from django.db.models import Count, F

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories():
    #categories = Category.objects.all()
    #TODO: понять как считать только опубликованные записи
    #categories = Category.objects.annotate(cnt=Count('get_news')).filter(cnt__gt=0)
    #филтрация количества опубликованных новостей
    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    return {'categories': categories}


