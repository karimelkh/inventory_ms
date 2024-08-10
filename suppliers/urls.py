from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="suppliers"),
    path("<str:id>", views.show, name="show_supplier"),
    path("new/", views.new, name="new_supplier"),
]
