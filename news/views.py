from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    return  HttpResponse("Hello people this is NEWS")

def test(request):
    return  HttpResponse("<H1>Тестовая страница</H1>")
