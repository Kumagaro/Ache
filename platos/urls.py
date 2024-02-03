from django.urls import path, re_path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("formulario_plato/", views.formulario_plato, name="formulario_plato"),
    path("formulario_Sub/", views.formulario_sub,  name="formulario_sub"),
    path("agregar_plato/", views.agregar_plato, name="agregar_plato"),
    path("agregar_sub/", views.agregar_sub, name="agregar_sub"),
    path("", views.eliminar, name="eliminar"),
    path("editar_plato/", views.editar_plato, name="editar_plato"),
    path("subcategorias/", views.subcategorias, name="subcategorias"),
    path("eliminar_categoria/", views.eliminar_categoria, name="eliminar_categoria"),
    path("mostrar_categoria/", views.mostrar_categoria, name="mostrar_categoria"),
]