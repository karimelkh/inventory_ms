from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from utils.count import get_count

from .forms import NewSiteForm
from .models import Site


@login_required
def show(req, id):
    if Site.objects.filter(site_id=id).exists():
        site = Site.objects.filter(site_id=id)
        # form = UpdateSiteForm(instance=item)
        # context = { "prod": prod[0], "form": form, "count": get_count() }
        context = {"site": site[0], "count": get_count(), "username": req.user.username}
        return render(req, "storagesites/show.html", context)
    return redirect("sites")


@login_required
def index(req):
    username = req.user.username
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
            new_site = Site.objects.filter(site_name=form.cleaned_data["site_name"])[0]
            messages.success(
                req,
                f"you have successfully created a site: {new_site.site_name}",
            )
            if action == "save":
                context = {"form": form}
            elif action == "save_quit":
                return redirect("show_site", id=new_site.site_id)
        else:
            form.add_error(None, "Form not valid!")
            context = {"form": form}
    else:
        form = NewSiteForm()
        context = {"form": form}
    return render(req, "storagesites/new.html", context)
