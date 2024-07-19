from django.shortcuts import render, redirect
from items.models import Item
from categories.models import Category
from suppliers.models import Supplier
from storagesites.models import Site
from .forms import NewSupplForm
from utils.count import get_count

def index(req):
    if req.user.is_authenticated:
        username = req.user.username
        suppls = Supplier.objects.all()
        context = { "suppls": suppls, "count": get_count() }
        return render(req, "suppliers/index.html", context)
    return redirect("/login/")


def new(req):
    if req.method == "POST":
        form = NewSupplForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            if action == "save":
                context = { "form": form }
            elif action == "save_quit":
                return redirect("/suppliers/")
        else:
            form.add_error(None, "Form not valid!")
            context = { "form": form }
    else:
        form = NewSupplForm()
        context = { "form": form }
    return render(req, "suppliers/new.html", context)
