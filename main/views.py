from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from utils.count import get_count 

@login_required
def home(req):
    username = req.user.username
    context = { "count": get_count(), "username": req.user.username }
    return render(req, "main/home.html", context)
