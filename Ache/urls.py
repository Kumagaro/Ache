from django.contrib import admin

#Librerias parar renderizar imagenes

from django.conf import settings
from django.views.static import serve

#Fin

from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("admin_ache/", views.admin, name="admin"),
    path("platos/", include("platos.urls")),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]