from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from utils.count import get_count

from .forms import NewProdForm, UpdateProdForm
from .models import Product


@login_required
def show(req, id):
    prod = get_object_or_404(Product, id=id)
    if req.method == "POST":
        if "rm" in req.POST:
            Product.objects.filter(id=id).delete()
            return redirect("prods")
        elif "ud" in req.POST:
            form = NewProdForm(req.POST, instance=prod)
            if form.is_valid():
                form.save()
            return redirect("show_prod", id=id)
    if Product.objects.filter(id=id).exists():
        prod = Product.objects.filter(id=id)
        form = NewProdForm(instance=prod[0])
        context = {
            "prod": prod[0],
            "form": form,
            "count": get_count(),
            "username": req.user.username,
        }
        return render(req, "products/show.html", context)
    return redirect("prods")


@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        print(f"Entire POST data: {req.POST}")
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Product.objects.filter(id=id).delete()
            elif action == "update":
                if "id" in req.POST:
                    prod = get_object_or_404(Product, id=req.POST.get("id"))
                    form = NewProdForm(req.POST, instance=prod)
                    if form.is_valid():
                        form.save()
                        messages.success(req, "Update Successed!")
                else:
                    messages.error(req, "Update Failed!")
            elif action == "getUpdateForm":
                prod = get_object_or_404(Product, id=req.POST.get("id"))
                update_form = UpdateProdForm(instance=prod)
                form_html = render_to_string("main/update_form.html", {"update_form": update_form})
                return JsonResponse({"form_html": form_html})
    prods = Product.objects.all()
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
