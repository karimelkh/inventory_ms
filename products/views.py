from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from utils.count import get_count

from .forms import NewProdForm, UpdateProdForm
from .models import Product


@login_required
@csrf_exempt
def show(req, id):
    prod = get_object_or_404(
        Product.objects.annotate(item_count=Count("item")),
        id=id
    )
    if req.method == "POST" and "action" in req.POST:
        action = req.POST.get("action")
        if action == "delete":
            Product.objects.filter(id=id).delete()
            return redirect("prods")
        if action == "update":
            form = UpdateProdForm(req.POST, req.FILES, instance=prod)
            if form.is_valid():
                form.save()
            return redirect("show_prod", id=id)
        elif action == "getUpdateForm":
            update_form = UpdateProdForm(instance=prod)
            form_html = render_to_string("main/update_form.html", {"update_form": update_form})
            return JsonResponse({"form_html": form_html})
        elif action == "getDelConfirm":
            message = f"Are you sure you want to delete: <b>{prod.ttl}</b>?"
            form_html = render_to_string("main/delete_form.html", {"confirm_message": message})
            return JsonResponse({"form_html": form_html})
    form = UpdateProdForm(instance=prod)
    context = {
        "prod": prod,
        "form": form,
        "count": get_count(),
        "username": req.user.username,
    }
    return render(req, "products/show.html", context)


@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Product.objects.filter(id=id).delete()
            elif action == "update":
                if "id" in req.POST:
                    prod = get_object_or_404(Product, id=req.POST.get("id"))
                    form = NewProdForm(req.POST, req.FILES, instance=prod)
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
                prod = get_object_or_404(Product, id=req.POST.get("id"))
                update_form = UpdateProdForm(instance=prod)
                form_html = render_to_string("main/update_form.html", {"update_form": update_form})
                return JsonResponse({"form_html": form_html})
    prods = Product.objects.annotate(item_count=Count("item"))
    context = {
            "prods": prods,
            "count": get_count(),
            "username": req.user.username,
            }
    return render(req, "products/index.html", context)


@login_required
def new(req):
    if req.method == "POST":
        form = NewProdForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            created_prod = Product.objects.filter(
                ttl=form.cleaned_data["ttl"]
            )[0]
            messages.success(
                req,
                f"You have created the prod {created_prod.ttl} successfully",
            )
            if action == "save":
                # context = {"form": form}
                pass
            elif action == "save_quit":
                return redirect("show_prod", id=created_prod.id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewProdForm()
        context = {"form": form}
    return render(req, "products/new.html", context)
