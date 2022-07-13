from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Usuario(models.Model):
    tipo_de_usuario = Administrador o cliente.
    correo_elec = models.CharField(max_length=40)
    clave =  models.CharField(max_length=40)
    apellido =  models.CharField(max_length=40)
    nombre =  models.CharField(max_length=40)
    fecha_nac = 
    nro_celular = models.IntegerField()
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)

class Producto(models.Model):
    id_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=40)
    categoria_producto = models.CharField(max_length=40)
    marca_producto = models.CharField(max_length=40)
    descripcion_producto= RichTextField()
    precio = models.IntegerField()
    cantidad_disponible = models.IntegerField()
    fotos_productos= models.ImageField(upload_to="producto", null=True, blank=True)
    responsable_carga = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
