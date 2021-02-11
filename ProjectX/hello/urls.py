from django.urls import path
from . import views #import views from current directory

#a list of accessible urls on the hello app
urlpatterns = [
    path("", views.index, name = "index"),
    path("brian", views.brian, name = "brian")

]