from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def jenn(request):
    return HttpResponse("Helllo, Jenn!")

def britnie(request):
    return HttpResponse("Hello, britnie!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
