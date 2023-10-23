from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworld(response):
    return HttpResponse("helloworld.html")
