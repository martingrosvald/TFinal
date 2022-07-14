from django import forms
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Agregar_Usuario (forms.Form):
    tipo_de_usuario = forms.CharField(max_length=40)
    clave =  forms.CharField(max_length=40)
    apellido =  forms.CharField(max_length=40)
    nombre =  forms.CharField(max_length=40)
    correo_elec = forms.EmailField(max_length=90)
    fecha_nac = forms.DateField()
    nro_celular = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=40)
    provincia = forms.CharField(max_length=40)
    codigo_postal = forms.CharField(max_length=40)
    pais = CountryField()

class Agregar_Producto (forms.Form):
    id_producto = forms.IntegerField()
    nombre_producto = forms.CharField(max_length=40)
    marca_producto = forms.CharField(max_length=40)
    descripcion_producto= RichTextField()
    precio = forms.IntegerField()
    cantidad_disponible = forms.IntegerField()
    responsable_carga = forms.CharField(max_length=40)
    fecha_creacion_producto = forms.DateField()
    fecha_actualiz = forms.DateField() 