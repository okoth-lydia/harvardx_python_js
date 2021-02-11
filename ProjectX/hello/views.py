from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#request argument represents the http request made to access server
def index(request,):
    return render(request, "hello/index.html")

#returns hello brian when the url is visited
def brian(request):
    return HttpResponse("Hello, Brian")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })    