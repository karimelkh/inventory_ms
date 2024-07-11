from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_v(req):
    if req.user.is_authenticated:
        return redirect("/home/")
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect("/home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    if form.errors and form.errors["__all__"]:
        # buggy place
        errors = form.errors["__all__"]
    else:
        errors = {}
    context = { "form": form, "errors": errors }
    return render(req, "users/login.html", context)


def logout_v(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            logout(req)
            return redirect("/login/")
        else:
            return render(req, "users/logout.html", {})
    else:
        return redirect("/login/")
