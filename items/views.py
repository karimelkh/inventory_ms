from django.shortcuts import render, redirect
from main.models import Supplier, Category, Location
from .forms import NewItemForm
from .models import Item

def new(req):
    if req.method == "POST":
        # 2nd time
        form = NewItemForm(req.POST, req.FILES)
        action = req.POST.get("action")
        print(f"action: {action}")
        if form.is_valid():
            # valid form
            id = form.cleaned_data["id"]
            ttl = form.cleaned_data["title"]
            desc = form.cleaned_data["description"]
            stock = form.cleaned_data["quantity"]
            img = form.cleaned_data["img"]
            suppl = form.cleaned_data["supplier"]
            cat = form.cleaned_data["category"]
            locat = form.cleaned_data["location"]
            new_item = Item(
                    prod_id = id,
                    prod_title = ttl,
                    prod_desc = desc,
                    stock = stock,
                    img = img,
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
