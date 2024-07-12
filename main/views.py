from django.shortcuts import render, redirect

def home(req):
    if req.user.is_authenticated:
        username = req.user.username
        context = {}
        return render(req, "main/home.html", context)
    else:
        return redirect("/login/")
