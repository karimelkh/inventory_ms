from django.shortcuts import render, redirect
from main.models import Supplier, Category, Location
from .forms import NewItemForm
from .models import Item

def index(req):
    if req.user.is_authenticated:
        username = req.user.username
        prods = Item.objects.all()
        i_count = Item.objects.count()
        c_count = Category.objects.count()
        s_count = Supplier.objects.count()
        l_count = Location.objects.count()
        o_count = 0
        prod_data = [
            {
                'id_prod': prod.prod_id,
                'prod_title': prod.prod_title,
                'prod_desc': prod.prod_desc,
                'qty_in_stock': prod.stock,
                'cat_id': prod.cat_id,
                'locat_id': prod.locat_id,
                'suppl_id': prod.suppl_id
            }
            for prod in prods
        ]
        context = {
            "prod_data": prod_data,
            "username": username,
            "items_count": i_count,
            "cats_count": c_count,
            "suppls_count": s_count,
            "locats_count": l_count,
            "orders_count": o_count,
        }
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
                return redirect("/home/")
        else:
            form.add_error(None, "Form not valid!")
            context = { "form": form }
    else:
        form = NewItemForm()
        context = { "form": form }
    return render(req, "items/new.html", context)
