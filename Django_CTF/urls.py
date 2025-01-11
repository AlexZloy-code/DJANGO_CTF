from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from DJANGO_CTF.views import custom_404_view

handler404 = custom_404_view 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("users/", include("users.urls")),
    path("tasks/", include("web_tasks.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)