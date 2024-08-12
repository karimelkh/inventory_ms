from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from utils.count import get_count

from .models import User
from .forms import LoginForm, NewUserForm


@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    User.objects.filter(id=id).delete()
            elif action == "update":
                user = get_object_or_404(User, id=req.POST.get("id"))
                form = NewUserForm(req.POST, instance=user)
                if form.is_valid:
                    form.save()
            elif action == "getUpdateForm":
                user = get_object_or_404(User, id=req.POST.get("id"))
                update_form = NewUserForm(instance=user)
                form_html = render_to_string("main/update_form.html", {"update_form": update_form})
                return JsonResponse({"form_html": form_html})

    users = User.objects.all()
    context = {"users": users, "count": get_count(), "username": req.user.username}
    return render(req, "users/index.html", context)


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
