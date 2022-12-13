from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("this is home page")

def product(request):
    return HttpResponse("this is product")

def contact(request):
    return HttpResponse("this is contact page")
