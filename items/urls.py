from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="items"),
    path("<int:id>", views.show, name="show_item"),
    path("new/", views.new, name="show_item"),
]

