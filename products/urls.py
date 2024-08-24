from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="prods"),
    path("<str:id>", views.show, name="show_prod"),
    path("new/", views.new, name="new_prod"),
]
