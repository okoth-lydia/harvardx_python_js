#import the datetime module
import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    #create a variable that accesses datetime now functionality
    now = datetime.datetime.now()
    return render(request, "NewYear/index.html", {
        "NewYear": now.month == 1 and now.day == 1
    })
