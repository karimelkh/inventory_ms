from django.shortcuts import render, redirect
from utils.count import get_count 

def home(req):
    if req.user.is_authenticated:
        username = req.user.username
        context = { "count": get_count() }
        return render(req, "main/home.html", context)
    else:
        return redirect("/login/")
