from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from action_logs.models import ActionLog
from utils.count import get_count

from .forms import NewSiteForm, UpdateSiteForm
from .models import Site, SiteType


@login_required
@csrf_exempt
def show(req, id):
    site = get_object_or_404(Site, id=id)
    if req.method == "POST" and "action" in req.POST:
        action = req.POST.get("action")
        if action == "delete":
            Site.objects.filter(id=id).delete()
            ActionLog.objects.create(
                user=req.user,
                action="delete",
                model_name="Site",
                object_id=id
            )
            return redirect("sites")
        if action == "update":
            form = UpdateSiteForm(req.POST, req.FILES, instance=site)
            if form.is_valid():
                form.save()
                ActionLog.objects.create(
                    user=req.user,
                    action="update",
                    model_name="Site",
                    object_id=id
                )
            return redirect("show_site", id=id)
        elif action == "getUpdateForm":
            update_form = UpdateSiteForm(instance=site)
            form_html = render_to_string("main/update_form.html", {"update_form": update_form})
            return JsonResponse({"form_html": form_html})
        elif action == "getDelConfirm":
            message = f"Are you sure you want to delete: <b>{site.name}</b> ?"
            form_html = render_to_string("main/delete_form.html", {"confirm_message": message})
            return JsonResponse({"form_html": form_html})
    form = UpdateSiteForm(instance=site)
    context = {
        "site": site,
        "form": form,
        "count": get_count(),
        "username": req.user.username,
    }
    return render(req, "storagesites/show.html", context)

@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Site.objects.filter(id=id).delete()
                    ActionLog.objects.create(
                        user=req.user,
                        action="delete",
                        model_name="Site",
                        object_id=id
                    )
            elif action == "update":
                if "id" in req.POST:
                    site = get_object_or_404(Site, id=req.POST.get('id'))
                    form = UpdateSiteForm(req.POST, req.FILES, instance=site)
                    if form.is_valid():
                        form.save()
                        ActionLog.objects.create(
                            user=req.user,
                            action="update",
                            model_name="Site",
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
                site = get_object_or_404(Site, id=req.POST.get("id"))
                update_form = UpdateSiteForm(instance=site)
                form_html = render_to_string("main/update_form.html", {"update_form": update_form})
                return JsonResponse({"form_html": form_html})
    sites = Site.objects.select_related("type").all();
    context = {"sites": sites, "count": get_count(), "username": req.user.username}
    return render(req, "storagesites/index.html", context)


@login_required
def new(req):
    if req.method == "POST":
        form = NewSiteForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            new_site = Site.objects.filter(id=form.cleaned_data["id"])[0]
            ActionLog.objects.create(
                user=req.user,
                action="create",
                model_name="Site",
                object_id=new_site.id
            )
            messages.success(
                req,
                f"you have successfully created a site: {new_site.name}",
            )
            if action == "save":
                context = {"form": form}
            elif action == "save_quit":
                return redirect("show_site", id=new_site.id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewSiteForm()
        context = {"form": form}
    return render(req, "storagesites/new.html", context)
