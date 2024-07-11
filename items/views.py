from django.shortcuts import render, redirect, HttpResponse
from main.models import Supplier, Category, Location
from .forms import NewItemForm
from .models import Item

def all_items(req):
    return HttpResponse("<h1>Items list:</h1>")

def show_item(req, item_id):
    return HttpResponse("<h1>%d</h1>" % item_id)

def new(req):
    if req.method == "GET":
        # 2nd time
        form = NewItemForm(req.GET)
        action = req.GET.get("action")
        print(f"action: {action}")
        if form.is_valid():
            # valid form
            id = form.cleaned_data["id"]
            ttl = form.cleaned_data["title"]
            desc = form.cleaned_data["description"]
            stock = form.cleaned_data["quantity"]
            suppl = form.cleaned_data["supplier"]
            cat = form.cleaned_data["category"]
            locat = form.cleaned_data["location"]
            new_item = Item(
                    prod_id = id,
                    prod_title = ttl,
                    prod_desc = desc,
                    stock = stock,
                    suppl = Supplier.objects.get(id_suppl=suppl),
                    cat = Category.objects.get(id_cat=cat),
                    locat = Location.objects.get(id_locat=locat)
                )
            new_item.save()
            if action == "save":
                # stay oon the page
                context = { "form": form }
            elif action == "save_quit":
                # go to /home/
                return redirect("/home/")
        else:
            # invlid form
            form.add_error(None, "Form not valid!")
            context = { "form": form }
    else: # 1st time
        form = NewItemForm()
        context = { "form": form }
    return render(req, "items/new.html", context)
 
# def new(req):
#     if req.method == "GET":
#         form = NewItemForm(req.GET)
#         action = req.GET.get("action")
#         if form.is_valid():
#             id = form.cleaned_data["id"]
#             ttl = form.cleaned_data["title"]
#             desc = form.cleaned_data["description"]
#             stock = form.cleaned_data["quantity"]
#             suppl = form.cleaned_data["supplier"]
#             cat = form.cleaned_data["category"]
#             locat = form.cleaned_data["location"]
#             new_item = Item(
#                     prod_id = id,
#                     prod_title = ttl,
#                     prod_desc = desc,
#                     stock = stock,
#                     suppl = Supplier.objects.get(id_suppl=suppl),
#                     cat = Category.objects.get(id_cat=cat),
#                     locat = Location.objects.get(id_locat=locat)
#                     )
#             new_item.save()
#            if action == "save_quit":
#                return redirect("/home/")
#            elif action == "save":
#                context = { "form": form }
#                pass
#        else:
#            context = { "form": form }
#    else:
#        form = NewItemForm()
#        context = { "form": form }
#    return render(req, "items/new.html", context)
