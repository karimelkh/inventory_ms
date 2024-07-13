from django.shortcuts import render, redirect
from main.models import Location
from items.models import Item
from categories.models import Category
from suppliers.models import Supplier
from .forms import NewSupplForm

def index(req):
    if req.user.is_authenticated:
        username = req.user.username
        suppls = Supplier.objects.all()
        i_count = Item.objects.count()
        c_count = Category.objects.count()
        s_count = Supplier.objects.count()
        l_count = Location.objects.count()
        o_count = 0
        context = {
            "suppls": suppls,
            "items_count": i_count,
            "cats_count": c_count,
            "suppls_count": s_count,
            "locats_count": l_count,
            "orders_count": o_count,
        }
        return render(req, "suppliers/index.html", context)
    else:
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
