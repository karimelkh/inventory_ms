from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect

from utils.count import get_count

from .forms import NewSiteForm
from .models import Site


@login_required
def show(req, id):
    if Site.objects.filter(id=id).exists():
        site = Site.objects.filter(id=id)
        context = {"site": site[0], "count": get_count(), "username": req.user.username}
        return render(req, "storagesites/show.html", context)
    print(f"SITE {id} DOES NOT EXISTS")
    return redirect("sites")


@login_required
@csrf_exempt
def index(req):
    if req.method == "POST":
        if "action" in req.POST:
            action = req.POST.get("action")
            if action == "remove":
                for id in req.POST.getlist("rm-id"):
                    Site.objects.filter(id=id).delete()
            elif action == "update":
                site = get_object_or_404(Site, name=req.POST.get("name"))
                form = NewSiteForm(req.POST, instance=site)
                if form.is_valid:
                    form.save()
            elif action == "getUpdateForm":
                site = get_object_or_404(Site, i=req.POST.get("id"))
                update_form = NewSiteForm(instance=site)
                form_html = render_to_string('main/update_form.html', {'update_form': update_form})
                return JsonResponse({'form_html': form_html})
    sites = Site.objects.all()
    context = {"sites": sites, "count": get_count(), "username": req.user.username}
    return render(req, "storagesites/index.html", context)


@login_required
def new(req):
    if req.method == "POST":
        form = NewSiteForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            new_site = Site.objects.filter(name=form.cleaned_data["name"])[0]
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
