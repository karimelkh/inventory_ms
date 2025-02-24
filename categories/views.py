from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from action_logs.models import ActionLog
from utils.count import get_count

from .forms import NewCatForm, UpdateCatForm
from .models import Category


@login_required
@csrf_exempt
def show(req, id):
    cat = get_object_or_404(Category, id=id)
    if req.method == "POST" and "action" in req.POST:
        action = req.POST.get("action")
        if action == "delete":
            Category.objects.filter(id=id).delete()
            ActionLog.objects.create(
                user=req.user,
                action="delete",
                model_name="Category",
                object_id=id
            )
            return redirect("cats")
        if action == "update":
            form = UpdateCatForm(req.POST, req.FILES, instance=cat)
            if form.is_valid():
                form.save()
            ActionLog.objects.create(
                user=req.user,
                action="update",
                model_name="Category",
                object_id=id
            )
            return redirect("show_cat", id=id)
        elif action == "getUpdateForm":
            update_form = UpdateCatForm(instance=cat)
            form_html = render_to_string("main/update_form.html", {"update_form": update_form})
            return JsonResponse({"form_html": form_html})
        elif action == "getDelConfirm":
            message = f"Are you sure you want to delete: <b>{cat.name}</b> ?"
            form_html = render_to_string("main/delete_form.html", {"confirm_message": message})
            return JsonResponse({"form_html": form_html})
    form = UpdateCatForm(instance=cat)
    context = {
        "cat": cat,
        "form": form,
        "count": get_count(),
        "username": req.user.username,
    }
    return render(req, "categories/show.html", context)

@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Category.objects.filter(id=id).delete()
                    ActionLog.objects.create(
                        user=req.user,
                        action="delete",
                        model_name="Category",
                        object_id=id
                    )
            elif action == "update":
                if "id" in req.POST:
                    cat = get_object_or_404(Category, id=req.POST.get("id"))
                    form = UpdateCatForm(req.POST, instance=cat)
                    if form.is_valid():
                        form.save()
                        ActionLog.objects.create(
                            user=req.user,
                            action="update",
                            model_name="Category",
                            object_id=req.POST.get("id")
                        )
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
                cat = get_object_or_404(Category, id=req.POST.get("id"))
                update_form = UpdateCatForm(instance=cat)
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
            new_cat = Category.objects.filter(id=form.cleaned_data["id"])[0]
            ActionLog.objects.create(
                user=req.user,
                action="create",
                model_name="Category",
                object_id=new_cat.id
            )
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
