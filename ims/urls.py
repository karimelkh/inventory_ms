from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("", include("users.urls")),
    path("items/", include("items.urls")),
    path("categories/", include("categories.urls")),
    path("cats/", include("categories.urls")),
    path("suppliers/", include("suppliers.urls")),
    path("sites/", include("storagesites.urls")),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
