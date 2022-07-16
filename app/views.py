from django.shortcuts import render
from app.forms import Agregar_Producto, Agregar_Usuario, Realizar_venta
from app.models import Producto, Usuario, Ventas
from ckeditor.fields import RichTextField
# Create your views here.

def altaProducto(request):
    if request.method == 'POST':
        agregar_producto = Agregar_Producto(request.POST)
        
        if agregar_producto.is_valid():
            informacion = agregar_producto.cleaned_data
            producto = Producto(id_producto=informacion["id_producto"], nombre_producto=informacion["nombre_producto"], categoria_producto=informacion["categoria_producto"],marca_producto=informacion["marca_producto"],precio=informacion["precio"],cantidad_disponible=informacion["cantidad_disponible"],fecha_creacion_producto=informacion["fecha_creacion_producto"])
            producto.save()
        return render (request, "app/listado_producto.html")
    
    else:
        agregar_producto= Agregar_Producto()
    return render (request,"app/agregar_producto.html",{"agregar_producto":agregar_producto})

def listar_producto(request):
    context= {}
    
    context["producto"] = Producto.objects.all()
    return render(request, "app/listado_producto.html", context)