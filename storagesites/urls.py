from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="sites"),
    path("<int:id>", views.show, name="show_site"),
    path("new/", views.new, name="new_site"),
]
