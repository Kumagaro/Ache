from django.shortcuts import render
from platos.models import Plato, SubCategoria

def index (request):
    espe = SubCategoria.objects.filter(categoria="Especiales")
    pla = Plato.objects.all()
    pla_espe_01 = []
    pla_espe_02 = []
    cont = 1
    for e in espe:
        pla_espe = Plato.objects.filter(subcategoria_id = e.id)
        for p in pla_espe:
            if cont % 2 != 0:
                pla_espe_01.append(p)
            else:
                pla_espe_02.append(p)
            cont+=1


    bebidas = SubCategoria.objects.filter(categoria="Bebidas")
    entrantes = SubCategoria.objects.filter(categoria="Entrantes")
    platos_principales = SubCategoria.objects.filter(categoria="Platos principales")
    postres = SubCategoria.objects.filter(categoria="Postres")

    return render(request, "index.html", {
        "especiales" : espe, 
        "platos" : pla,
        "bebidas" : bebidas,
        "entrantes" : entrantes,
        "platos_principales" : platos_principales,
        "postres" : postres,
        "pla_espe_01" : pla_espe_01,
        "pla_espe_02" : pla_espe_02,
        })

def admin (request):

    pla = Plato.objects.all()
    sub = SubCategoria.objects.all()

    return render(request, "admin.html", {"platos": pla, "sub" : sub})
