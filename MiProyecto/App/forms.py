from django import forms
from .models import *

class Crear_Artista_forms(forms.Form):
    nombre = forms.CharField(max_length=100)

class Crear_Genero_forms(forms.Form):
    nombre = forms.CharField(max_length=100)

class Crear_Album_forms(forms.Form):
    titulo = forms.CharField(max_length=100)
    artista = forms.ModelChoiceField(queryset=Artista.objects.all())
    genero = forms.ModelChoiceField(queryset=Genero.objects.all())
    fecha_lanzamiento = forms.DateField()

class Crear_Cancion_forms(forms.Form):
    titulo = forms.CharField(max_length=100)
    album = forms.ModelChoiceField(queryset=Album.objects.all())

class Crear_Usuario_forms(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=10)

class Crear_Compra_forms(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all())
    album = forms.ModelChoiceField(queryset=Album.objects.all())
