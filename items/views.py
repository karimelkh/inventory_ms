from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from utils.count import get_count

from .forms import NewItemForm, UpdateItemForm
from .models import Item


@login_required
def show(req, id):
    item = get_object_or_404(Item, prod_id=id)
    if req.method == "POST":
        if "rm" in req.POST:
            Item.objects.filter(prod_id=id).delete()
            return redirect("items")
        elif "ud" in req.POST:
            form = UpdateItemForm(req.POST, instance=item)
            if form.is_valid:
                form.save()
            return redirect("show_item", id=id)
    if Item.objects.filter(prod_id=id).exists():
        prod = Item.objects.select_related("cat", "suppl", "locat").filter(prod_id=id)
        form = UpdateItemForm(instance=item)
        context = {
            "prod": prod[0],
            "form": form,
            "count": get_count(),
            "username": req.user.username,
        }
        return render(req, "items/show.html", context)
    return redirect("items")


@login_required
def index(req):
    if req.method == "POST":
        for id in req.POST.getlist("rm-id"):
            Item.objects.filter(prod_id=id).delete()
    prods = Item.objects.select_related("cat", "suppl", "locat").all()
    context = {
        "prod_data": prods,
        "count": get_count(),
        "username": req.user.username,
    }
    return render(req, "items/index.html", context)


@login_required
def new(req):
    if req.method == "POST":
        form = NewItemForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            created_item = Item.objects.filter(
                prod_title=form.cleaned_data["prod_title"]
            )[0]
            messages.success(
                req,
                f"You have created the item {created_item.prod_title} successfully",
            )
            if action == "save":
                # context = {"form": form}
                pass
            elif action == "save_quit":
                return redirect("show_item", id=created_item.prod_id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewItemForm()
        context = {"form": form}
    return render(req, "items/new.html", context)
