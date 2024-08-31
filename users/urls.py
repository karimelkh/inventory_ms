from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_v, name="login"),
    path("logout/", views.logout_v, name="logout"),
    path("users/", views.index, name="users"),
    path("users/new/", views.new, name="new_user"),
    path("users/<str:username>/", views.show, name="show_user"),
    path("users/@<str:username>/", views.show, name="show_user"),
]
