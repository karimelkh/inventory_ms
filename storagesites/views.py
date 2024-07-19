from django.shortcuts import render, redirect
from items.models import Item
from categories.models import Category
from suppliers.models import Supplier
from .models import Site
from .forms import NewSiteForm
from utils.count import get_count

def index(req):
    if req.user.is_authenticated:
        username = req.user.username
        sites = Site.objects.all()
        context = { "sites": sites, "count": get_count() }
        return render(req, "storagesites/index.html", context)
    return redirect("/login/")


def new(req):
    if req.method == "POST":
        form = NewSiteForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            if action == "save":
                context = { "form": form }
            elif action == "save_quit":
                return redirect("/sites/")
        else:
            form.add_error(None, "Form not valid!")
            context = { "form": form }
    else:
        form = NewSiteForm()
        context = { "form": form }
    return render(req, "storagesites/new.html", context)
