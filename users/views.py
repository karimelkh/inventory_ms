from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from utils.count import get_count

from .models import User
from .forms import LoginForm, NewUserForm


@login_required
def index(req):
    if req.user.is_authenticated:
        users = User.objects.all()
        context = {"users": users, "count": get_count(), "username": req.user.username}
        return render(req, "users/index.html", context)
    return redirect("login")


@login_required
def new(req):
    if req.method == "POST":
        form = NewUserForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            created_user = form.cleaned_data["username"]
            messages.success(
                req, f"You have created the user {created_user} successfully"
            )
            if action == "save":
                pass
            elif action == "save_quit":
                return redirect("show_user", username=created_user)
        else:
            form.add_error(None, "Form not valid!")
    else:
        form = NewUserForm()
    context = {"form": form}
    return render(req, "users/new.html", context)


@login_required
def show(req, username):
    user = get_object_or_404(User, username=username)
    context = {"user": user, "count": get_count(), "username": req.user.username}
    return render(req, "users/show.html", context)


def login_v(req):
    if req.user.is_authenticated:
        return redirect("home")
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect("home")
            form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    if form.errors and form.errors["__all__"]:
        # buggy place
        errors = form.errors["__all__"]
    else:
        errors = {}
    context = {"form": form, "errors": errors}
    return render(req, "users/login.html", context)


@login_required
def logout_v(req):
    if req.method == "POST":
        logout(req)
        return redirect("login")
    return render(req, "users/logout.html", {})
