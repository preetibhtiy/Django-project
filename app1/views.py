from django.shortcuts import render
from .models import *
from .admin import *


# Create your views here.
def home(request):
    return render(request,"app1/home.html")  