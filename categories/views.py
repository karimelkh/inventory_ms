from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from items.models import Item
from categories.models import Category
from suppliers.models import Supplier
from storagesites.models import Site
from .forms import NewCatForm
from utils.count import get_count

@login_required
def index(req):
    username = req.user.username
    cats = Category.objects.all()
    context = { "cats": cats, "count": get_count() }
    return render(req, "categories/index.html", context)

@login_required
def new(req):
    if req.method == "POST":
        form = NewCatForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            if action == "save":
                context = { "form": form }
            elif action == "save_quit":
                return redirect("/categories/")
        else:
            form.add_error(None, "Form not valid!")
            context = { "form": form }
    else:
        form = NewCatForm()
        context = { "form": form }
    return render(req, "categories/new.html", context)
