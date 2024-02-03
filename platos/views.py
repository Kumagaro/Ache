from django.shortcuts import render
from django.http import HttpResponse
from .models import Plato, SubCategoria

def formulario_plato (request):
    sub = SubCategoria.objects.all().order_by("categoria")
    return render(request, "formulario_plato.html", {
        "sub" : sub,
    })

def formulario_sub (request):
    return render(request, "formulario_sub.html", {})

def agregar_sub (request):
    if request.method != "POST":
        return HttpResponse("Error")
    name = request.POST["name"]
    categoria = request.POST["categoria"]
    subcategoria = SubCategoria(name=name, categoria=categoria)
    subcategoria.save()
    sub = SubCategoria.objects.all()
    return render(request, "formulario_sub.html", {"subcategoria" : sub})

def agregar_plato (request):
    if request.method != "POST":
        return HttpResponse("Error")
    name = request.POST["name"]
    historia = request.POST["historia"]
    precio = request.POST["precio"]
    tiempo_elaboracion = request.POST["tiempo_elaboracion"]
    subcategoria = SubCategoria.objects.get(name = request.POST["subcategoria"])
    imagen = request.FILES.get("img")
    plato = Plato(name=name, historia=historia, precio=precio, tiempo_elaboracion=tiempo_elaboracion, disponible=True, imagen=imagen,subcategoria=subcategoria)
    plato.save()
    pla = Plato.objects.all() 
    sub = SubCategoria.objects.all()
    return render(request, "admin.html", {"platos" : pla, "sub" : sub})

def eliminar (request):
    if request.method != "POST":
        return HttpResponse("Error")
    plato = Plato.objects.get(name = request.POST["plato"])
    plato.delete()
    pla = Plato.objects.all()
    return render(request, "admin.html", {"platos" : pla})

def editar_plato (request):
    if request.method != "POST":
        plato = Plato.objects.get(name = request.GET["name"])

        return render(request, "editar_plato.html", {
            "name" : plato.name,
            "historia" : plato.historia,
            "precio" : plato.precio,
            "disponible" : plato.disponible,
            "tiempo" : plato.tiempo_elaboracion,
            "id" : plato.id,
        })
    plato = Plato.objects.get(id= request.POST["id"])
    if request.POST["name"] != "":
        plato.name = request.POST["name"]

    if request.POST["precio"] != "":
        plato.precio = request.POST["precio"]

    if request.POST["tiempo_elaboracion"] != "":
        plato.tiempo_elaboracion = request.POST["tiempo_elaboracion"]

    if request.POST["historia"] != "":
        plato.historia = request.POST["historia"]

    if request.POST.get("no_disponible", False):
        plato.disponible = False

    elif request.POST.get("disponible", False):
        plato.disponible = True
    
    imagen = request.FILES.get("img")

    plato.save()
    pla = Plato.objects.all()
    return render(request, "admin.html", {"platos" : pla})

def subcategorias (request):
    sub = SubCategoria.objects.all()
    return render(request, "subcategorias.html", {"sub" : sub})

def eliminar_categoria (request):
    if request.method != "POST":
        return HttpResponse("Error")
    sub = SubCategoria.objects.get(id = request.POST["sub"])
    sub.delete()
    sub = SubCategoria.objects.all()
    return render(request, "subcategorias.html", {"sub" : sub})

def mostrar_categoria (request):
    sub = SubCategoria.objects.get(id= request.POST["id"])
    if sub.activa:
        sub.activa = False

    else:
        sub.activa = True
    sub.save()
    sub = SubCategoria.objects.all()
    return render(request, "subcategorias.html", {"sub" : sub})
    pass