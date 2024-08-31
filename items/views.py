from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from utils.count import get_count

from .forms import NewItemForm, UpdateItemForm
from .models import Item


@login_required
@csrf_exempt
def show(req, id):
    item = get_object_or_404(Item, id=id)
    if req.method == "POST" and "action" in req.POST:
        action = req.POST.get("action")
        if action == "delete":
            Item.objects.filter(id=id).delete()
            return redirect("items")
        elif action == "update":
            form = UpdateItemForm(req.POST, req.FILES, instance=item)
            if form.is_valid():
                form.save()
            return redirect("show_item", id=id)
        elif action == "getUpdateForm":
            update_form = UpdateItemForm(instance=item)
            form_html = render_to_string("main/update_form.html", {"update_form": update_form})
            return JsonResponse({"form_html": form_html})
        if action == "getDelConfirm":
            message = f"Are you sure you want to delete: <b>{item.ttl}</b> ?"
            form_html = render_to_string("main/delete_form.html", {"confirm_message": message})
            return JsonResponse({"form_html": form_html})
    if Item.objects.filter(id=id).exists():
        item = Item.objects.select_related("prod", "cat", "suppl", "site").filter(id=id)
        form = UpdateItemForm(instance=item[0])
        context = {
             # TODO: change prod to item
            "prod": item[0],
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
                if "id" in req.POST:
                    item = get_object_or_404(Item, id=req.POST.get("id"))
                    form = UpdateItemForm(req.POST, req.FILES, instance=item)
                    if form.is_valid():
                        form.save()
                        messages.success(req, "Update Successed!")
                    else:
                        if form.errors:
                            for field, errors in form.errors.items():
                                for error in errors:
                                    messages.error(req, f"{field}: {error}")
                        if form.non_field_errors():
                            for error in form.non_field_errors():
                                messages.error(req, error)
            elif action == "getUpdateForm":
                item = get_object_or_404(Item, id=req.POST.get("id"))
                update_form = UpdateItemForm(instance=item)
                form_html = render_to_string("main/update_form.html", {"update_form": update_form})
                return JsonResponse({"form_html": form_html})
    items = Item.objects.select_related("cat", "suppl", "site", "prod").all()
    context = {
            "items": items,
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
