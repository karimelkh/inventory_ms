from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from categories.models import Category
from utils.count import get_count

from .forms import NewCatForm


@login_required
def show(req, id):
    if Category.objects.filter(cat_id=id).exists():
        cat = Category.objects.filter(cat_id=id)
        # form = UpdateCatForm(instance=item)
        # context = { "prod": prod[0], "form": form, "count": get_count() }
        context = {"cat": cat[0], "count": get_count(), "username": req.user.username}
        return render(req, "categories/show.html", context)
    return redirect("categories")


@login_required
def index(req):
    cats = Category.objects.all()
    context = {"cats": cats, "count": get_count(), "username": req.user.username}
    return render(req, "categories/index.html", context)


@login_required
def new(req):
    if req.method == "POST":
        form = NewCatForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            new_cat = Category.objects.filter(cat_name=form.cleaned_data["cat_name"])[0]
            messages.success(
                req, f"You have successfully created the {new_cat.cat_name} category"
            )
            if action == "save":
                context = {"form": form}
            elif action == "save_quit":
                return redirect("show_cat", id=new_cat.cat_id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewCatForm()
        context = {"form": form}
    return render(req, "categories/new.html", context)
