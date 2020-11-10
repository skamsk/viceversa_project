from django.http import  HttpResponse
from django.shortcuts import render

def about(request):
    return  HttpResponse("Hello people")

def home(request):
    return render(request, 'home.html', {"gosha":"PZDC"})

def reverse(request):
    text = request.GET['usertext']
    get_text = text[::-1]
    return render(request, 'reverse.html', {'user_text':text, 'reverse_text':get_text})