from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("", include("users.urls")),
    path("items/", include("items.urls")),
    path("categories/", include("categories.urls")),
    path("cats/", include("categories.urls")),
]

urlpatterns += staticfiles_urlpatterns()
