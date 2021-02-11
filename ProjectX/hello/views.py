from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#request argument represents the http request made to access server
def index(request):
    return HttpResponse("Hello World")

#returns hello brian when the url is visited
def brian(request):
    return HttpResponse("Hello, Brian")