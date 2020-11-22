from  django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', test, name='about'),
    path('category/<int:category_id>/', get_category, name='category'),
]