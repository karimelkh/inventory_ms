from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="suppliers"),
    path("<int:id>", views.show, name="show_supplier"),
    path("new/", views.new, name="new_supplier"),
]
