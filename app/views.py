from django.shortcuts import render
from app.forms import Agregar_Producto
from app.models import Producto
from ckeditor.fields import RichTextField
# Create your views here.

def altaProducto(request):
    if request.method == 'POST':
        agregar_producto = Agregar_Producto(request.POST)

        if agregar_producto.is_valid():
            informacion = agregar_producto.cleaned_data
            producto = Producto(nombre=informacion["nombre_producto"], cantidad=informacion["cantidad_diponible"],)
            producto.save()
        return render (request, "app/listado_producto.html")
    
    else:
        agregar_producto= Agregar_Producto()
    return render (request,"app/agregar_producto.html",{"agregar_producto":agregar_producto})

def listar_producto(request):
    context= {}
    
    context["producto"] = Producto.objects.all()
    return render(request, "app/listado_producto.html", context)