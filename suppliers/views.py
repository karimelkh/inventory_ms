from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from utils.count import get_count

from .forms import NewSupplForm
from .models import Supplier


@login_required
def show(req, id):
    if Supplier.objects.filter(suppl_id=id).exists():
        suppl = Supplier.objects.filter(suppl_id=id)
        # form = UpdateSupplierForm(instance=item)
        # context = { "suppl": suppl[0], "form": form, "count": get_count() }
        context = {
            "suppl": suppl[0],
            "count": get_count(),
            "username": req.user.username,
        }
        return render(req, "suppliers/show.html", context)
    return redirect("suppliers")


@login_required
def index(req):
    username = req.user.username
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
            new_s = Supplier.objects.filter(suppl_name=form.cleaned_data["suppl_name"])[
                0
            ]
            messages.success(
                req,
                f"You have successfully created a supplier: {new_s.suppl_name}",
            )
            if action == "save":
                context = {"form": form}
            elif action == "save_quit":
                return redirect("show_supplier", id=new_s.suppl_id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewSupplForm()
        context = {"form": form}
    return render(req, "suppliers/new.html", context)
