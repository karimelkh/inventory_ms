from django.shortcuts import render, redirect
from items.models import Item
from categories.models import Category
from suppliers.models import Supplier
from .models import Site
from .forms import NewSiteForm

def index(req):
    if req.user.is_authenticated:
        username = req.user.username
        sites = Site.objects.all()
        i_count = Item.objects.count()
        c_count = Category.objects.count()
        s_count = Supplier.objects.count()
        l_count = Site.objects.count()
        o_count = 0
        context = {
            "sites": sites,
            "items_count": i_count,
            "cats_count": c_count,
            "suppls_count": s_count,
            "locats_count": l_count,
            "orders_count": o_count,
        }
        return render(req, "storagesites/index.html", context)
    else:
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
