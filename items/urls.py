from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_items),
    path("new/", views.new),
    path("<int:id>", views.show_item),
]

