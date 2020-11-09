from django.http import  HttpResponse
from django.shortcuts import render

def about(request):
    return  HttpResponse("Hello people")

def home(request):
    return render(request, 'home.html', {"gosha":"PZDC"})