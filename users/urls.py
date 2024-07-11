from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_v),
    path("logout/", views.logout_v),
]
