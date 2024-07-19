from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import NewItemForm, UpdateItemForm
from categories.models import Category
from suppliers.models import Supplier
from storagesites.models import Site
from utils.count import get_count


def show_item(req, id):
    if req.user.is_authenticated:
        item = get_object_or_404(Item, prod_id=id)
        if req.method == "POST":
            if "rm" in req.POST:
                Item.objects.filter(prod_id=id).delete()
                return redirect("/items/")
            elif "ud" in req.POST:
                form = UpdateItemForm(req.POST, instance=item)
                if form.is_valid:
                    form.save()
                return redirect("show_item", id=id)
        if Item.objects.filter(prod_id=id).exists():
            prod = Item.objects.select_related("cat", "suppl", "locat").filter(prod_id=id)
            form = UpdateItemForm(instance=item)
            context = { "prod": prod[0], "form": form, "count": get_count() }
            return render(req, "items/show_item.html", context)
        return redirect("/items/")
    return redirect("/login/")


def index(req):
    if req.user.is_authenticated:
        prods = Item.objects.select_related("cat", "suppl", "locat").all()
        context = { "prod_data": prods , "count": get_count() }
        return render(req, "items/index.html", context)
    else:
        return redirect("/login/")


def new(req):
    if req.method == "POST":
        form = NewItemForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            if action == "save":
                context = { "form": form }
            elif action == "save_quit":
                return redirect("/items/")
        else:
            form.add_error(None, "Form not valid!")
            context = { "form": form }
    else:
        form = NewItemForm()
        context = { "form": form }
    return render(req, "items/new.html", context)
