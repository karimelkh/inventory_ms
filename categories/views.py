from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from categories.models import Category
from utils.count import get_count

from .forms import NewCatForm


@login_required
def show(req, id):
    if Category.objects.filter(id=id).exists():
        cat = Category.objects.filter(id=id)
        context = {"cat": cat[0], "count": get_count(), "username": req.user.username}
        return render(req, "categories/show.html", context)
    return redirect("categories")


@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Category.objects.filter(id=id).delete()
            elif action == "update":
                # the title should not be unique, to FIND a better way to do this
                cat = get_object_or_404(Category, name=req.POST.get("name"))
                form = NewCatForm(req.POST, instance=cat)
                if form.is_valid:
                    form.save()
            elif action == "getUpdateForm":
                cat = get_object_or_404(Category, id=req.POST.get("id"))
                update_form = NewCatForm(instance=cat)
                form_html = render_to_string('main/update_form.html', {'update_form': update_form})
                return JsonResponse({'form_html': form_html})
    cats = Category.objects.all()
    context = {
            "cats": cats,
            "count": get_count(),
            "username": req.user.username
        }
    return render(req, "categories/index.html", context)



@login_required
def new(req):
    if req.method == "POST":
        form = NewCatForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            new_cat = Category.objects.filter(name=form.cleaned_data["name"])[0]
            messages.success(
                req, f"You have successfully created the {new_cat.name} category"
            )
            if action == "save":
                context = {"form": form}
            elif action == "save_quit":
                return redirect("show_cat", id=new_cat.id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewCatForm()
        context = {"form": form}
    return render(req, "categories/new.html", context)
