from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from utils.count import get_count

from .forms import NewItemForm
from .models import Item


@login_required
def show(req, id):
    item = get_object_or_404(Item, id=id)
    if req.method == "POST":
        if "rm" in req.POST:
            Item.objects.filter(id=id).delete()
            return redirect("items")
        elif "ud" in req.POST:
            form = NewItemForm(req.POST, instance=item)
            if form.is_valid:
                form.save()
            return redirect("show_item", id=id)
    if Item.objects.filter(id=id).exists():
        prod = Item.objects.select_related("cat", "suppl", "site").filter(id=id)
        form = NewItemForm(instance=item)
        context = {
            "prod": prod[0],
            "form": form,
            "count": get_count(),
            "username": req.user.username,
        }
        return render(req, "items/show.html", context)
    return redirect("items")


@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Item.objects.filter(id=id).delete()
            elif action == "update":
                # the title should not be unique, to FIND a better way to do this
                item = get_object_or_404(Item, ttl=req.POST.get("ttl"))
                form = NewItemForm(req.POST, instance=item)
                if form.is_valid:
                    form.save()
                # pass
            elif action == "getUpdateForm":
                item = get_object_or_404(Item, id=req.POST.get("id"))
                update_form = NewItemForm(instance=item)
                form_html = render_to_string('main/update_form.html', {'update_form': update_form})
                return JsonResponse({'form_html': form_html})
    prods = Item.objects.select_related("cat", "suppl", "site").all()
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
                ttl=form.cleaned_data["ttl"]
            )[0]
            messages.success(
                req,
                f"You have created the item {created_item.ttl} successfully",
            )
            if action == "save":
                # context = {"form": form}
                pass
            elif action == "save_quit":
                return redirect("show_item", id=created_item.id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewItemForm()
        context = {"form": form}
    return render(req, "items/new.html", context)
