from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, NewUserForm
from utils.count import get_count 

def index(req):
    if req.user.is_authenticated:
        users = User.objects.all()
        context = { "users": users, "count": get_count() }
        return render(req, "users/index.html", context)
    return redirect("login")


def new(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = NewUserForm(req.POST, req.FILES)
            action = req.POST.get("action")
            if form.is_valid():
                form.save()
                if action == "save":
                    context = { "form": form }
                elif action == "save_quit":
                    # messages.success(req, 'You have singed up successfully.')
                    return redirect("show_user", username=form.cleaned_data['username'])
            form.add_error(None, "Form not valid!")
        else:
            form = NewUserForm()
        context = { "form": form }
        return render(req, "users/new.html", context)
    return redirect("login")


def show_user(req, username):
    if req.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        context = { "user": user, "count": get_count() }
        return render(req, "users/show.html", context)
    return redirect("login")


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
            return redirect("login")
        return render(req, "users/logout.html", {})
    return redirect("login")
