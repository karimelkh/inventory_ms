from django.shortcuts import render
from . import models

def home(req):
    home_dict = {}
    return render(req, 'main/home.html', home_dict)

def login(req):
    return render(req, 'main/login.html')
