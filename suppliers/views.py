from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from utils.count import get_count

from .forms import NewSupplForm, UpdateSupplForm
from .models import Supplier


@login_required
@csrf_exempt
def show(req, id):
    suppl = get_object_or_404(Supplier, id=id)
    if req.method == "POST" and "action" in req.POST:
        action = req.POST.get("action")
        if action == "delete":
            Supplier.objects.filter(id=id).delete()
            return redirect("suppliers")
        if action == "update":
            form = UpdateSupplForm(req.POST, req.FILES, instance=suppl)
            if form.is_valid():
                form.save()
            return redirect("show_supplier", id=id)
        elif action == "getUpdateForm":
            update_form = UpdateSupplForm(instance=suppl)
            form_html = render_to_string("main/update_form.html", {"update_form": update_form})
            return JsonResponse({"form_html": form_html})
    form = UpdateSupplForm(instance=suppl)
    context = {
        "suppl": suppl,
        "form": form,
        "count": get_count(),
        "username": req.user.username,
    }
    return render(req, "suppliers/show.html", context)

@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Supplier.objects.filter(id=id).delete()
            elif action == "update":
                if "id" in req.POST:
                    s = get_object_or_404(Supplier, id=req.POST.get("id"))
                    form = UpdateSupplForm(req.POST, req.FILES, instance=s)
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
                s = get_object_or_404(Supplier, id=req.POST.get("id"))
                update_form = UpdateSupplForm(instance=s)
                form_html = render_to_string('main/update_form.html', {'update_form': update_form})
                return JsonResponse({'form_html': form_html})
    suppls = Supplier.objects.all()
    context = {"suppls": suppls, "count": get_count(), "username": req.user.username}
    return render(req, "suppliers/index.html", context)


@login_required
def new(req):
    if req.method == "POST":
        form = NewSupplForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            new_s = Supplier.objects.filter(name=form.cleaned_data["name"])[
                0
            ]
            messages.success(
                req,
                f"You have successfully created a supplier: {new_s.name}",
            )
            if action == "save":
                context = {"form": form}
            elif action == "save_quit":
                return redirect("show_supplier", id=new_s.id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewSupplForm()
        context = {"form": form}
    return render(req, "suppliers/new.html", context)
