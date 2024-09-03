from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from action_logs.models import ActionLog
from utils.count import get_count 

@login_required
def home(req):
    recent_logs = ActionLog.objects.order_by("-timestamp")[:10]
    context = {
        "recent_logs": recent_logs,
        "count": get_count(),
        "username": req.user.username,
    }
    return render(req, "main/home.html", context)
