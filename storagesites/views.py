from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Site
from .forms import NewSiteForm
from utils.count import get_count

@login_required
def show(req, id):
    if Site.objects.filter(site_id=id).exists():
        site = Site.objects.filter(site_id=id)
        # form = UpdateSiteForm(instance=item)
        # context = { "prod": prod[0], "form": form, "count": get_count() }
        context = { "site": site[0], "count": get_count(), "username": req.user.username }
        return render(req, "storagesites/show.html", context)
    return redirect("sites")

@login_required
def index(req):
    username = req.user.username
    sites = Site.objects.all()
    context = { "sites": sites, "count": get_count(), "username": req.user.username }
    return render(req, "storagesites/index.html", context)

@login_required
def new(req):
    if req.method == "POST":
        form = NewSiteForm(req.POST, req.FILES)
        action = req.POST.get("action")
        if form.is_valid():
            form.save()
            if action == "save":
                context = { "form": form }
            elif action == "save_quit":
                return redirect("/sites/")
        else:
            form.add_error(None, "Form not valid!")
            context = { "form": form }
    else:
        form = NewSiteForm()
        context = { "form": form }
    return render(req, "storagesites/new.html", context)
