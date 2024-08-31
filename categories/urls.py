from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="categories"),
    path("", views.index, name="cats"),
    path("<str:id>", views.show, name="show_cat"),
    path("new/", views.new, name="new_cat"),
]
