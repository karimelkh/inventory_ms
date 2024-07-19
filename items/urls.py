from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.show_item, name="show_item"),
    path("new/", views.new),
]

