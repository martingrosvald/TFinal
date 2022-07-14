from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


# Create your models here.

class Usuario(models.Model):
    #t_usuario = [
    #    (ADMINISTRADOR, "Administrador"),
    #    (CLIENTE, "Cliente"),
    #    ]
    #tipo_de_usuario = models.CharField(
    #    max_length=20,
    #    choices=t_usuario, 
    #    default=CLIENTE,
    #    )
    tipo_de_usuario = models.CharField(max_length=40)
    clave =  models.CharField(max_length=40)
    apellido =  models.CharField(max_length=40)
    nombre =  models.CharField(max_length=40)
    correo_elec = models.EmailField(max_length=90)
    fecha_nac = models.DateField()
    nro_celular = models.IntegerField()
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=40)
    pais = CountryField()

class Producto(models.Model):
    id_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=40)
    #categoria_producto = models.CharField(
    #    choices=(
    #        (1, _("Textil")), 
    #        (2, _("Elementos de pesca")),
    #        (3, _("Accesorios"))
    #        ), 
    #    default=1
    #    )
    marca_producto = models.CharField(max_length=40)
    descripcion_producto= RichTextField()
    precio = models.IntegerField()
    cantidad_disponible = models.IntegerField()
    #fotos_productos= models.ImageField(upload_to="productos", null=True, blank=True)
    responsable_carga = models.CharField(max_length=40)
    fecha_creacion_producto = models.DateField()
    fecha_actualiz = models.DateField() 

#class Ventas (models.Model):
    #fecha_venta = models.DateField()
    #usuario_vendedor = Usuario()
    #detalle_venta = Producto() #como poner la cantidad de cada producto
    pass

#class Historial_stock(models.Model, Producto, Usuario):
    #fecha_movimiento = Producto.fecha_actualiz()
    #producto_movimiento = Producto.nombre_producto()
    #responsable_movimiento = Producto.responsable_carga()
    #tipo_mov = Venta() o Producto()
    #cantidad = poner el cambio en la cantidad del producto
    pass