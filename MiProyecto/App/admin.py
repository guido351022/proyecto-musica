from django.contrib import admin
from .models import Artista, Genero, Album, Cancion, Usuario, Compra

class CancionInline(admin.TabularInline):
    model = Cancion
    extra = 1  # Número de formularios adicionales para agregar canciones

class AlbumAdmin(admin.ModelAdmin):
    inlines = [CancionInline]  # Permite agregar canciones directamente en el álbum
    list_display = ('titulo', 'artista', 'genero', 'fecha_lanzamiento')  # Campos a mostrar en la lista
    search_fields = ('titulo',)  # Permite buscar álbumes por título
    list_filter = ('artista', 'genero')  # Permite filtrar álbumes por artista y género


admin.site.register(Artista)
admin.site.register(Genero)
admin.site.register(Album, AlbumAdmin)  # Usamos AlbumAdmin para mostrar el inline de canciones
admin.site.register(Cancion)
admin.site.register(Usuario)
admin.site.register(Compra)
