from django.urls import path
from App import views

urlpatterns = [
    path('', views.mostrar_index, name='Home'),
    path('usuario/', views.mostrar_usuario, name='Usuario'),
    path('artista/', views.mostrar_artista, name='Artista'),
    path('album/', views.mostrar_album, name='Album'),
    path('cancion/', views.mostrar_cancion, name='Cancion'),
    path('genero/', views.mostrar_genero, name='Genero'),
    path('compra/', views.mostrar_compra, name='Compra'),
    path('crear_usuario/', views.crear_usuario, name='Crear Usuario'),
    path('crear_artista/', views.crear_artista, name='Crear Artista'),
    path('crear_album/', views.crear_album, name='Crear Album'),
    path('crear_cancion/', views.crear_cancion, name='Crear Cancion'),
    path('crear_genero/', views.crear_genero, name='Crear Genero'),
    path('crear_compra/', views.crear_compra, name='Crear Compra'),
    path('buscar_artista/', views.buscar_artista, name='Buscar Artista'),
    path('buscar_genero/', views.buscar_genero, name='Buscar Genero'),
    path('buscar_album/', views.buscar_album, name='Buscar Album'),
    path('buscar_cancion/', views.buscar_cancion, name='Buscar Cancion'),
    path('buscar_usuario/', views.buscar_usuario, name='Buscar Usuario'),
    path('buscar_compra/', views.buscar_compra, name='Buscar Compra'),
    path('actualizar_artista/<int:artista_id>/', views.actualizar_artista, name='Actualizar Artista'),
    path('actualizar_genero/<int:genero_id>/', views.actualizar_genero, name='Actualizar Genero'),
    path('actualizar_album/<int:album_id>/', views.actualizar_album, name='Actualizar Album'),
    path('actualizar_cancion/<int:cancion_id>/', views.actualizar_cancion, name='Actualizar Cancion'),
    path('actualizar_usuario/<int:usuario_id>/', views.actualizar_usuario, name='Actualizar Usuario'),
    path('actualizar_compra/<int:compra_id>/', views.actualizar_compra, name='Actualizar Compra'),
    path('eliminar_artista/<int:artista_id>/', views.eliminar_artista, name='Eliminar Artista'),
    path('eliminar_genero/<int:genero_id>/', views.eliminar_genero, name='Eliminar Genero'),
    path('eliminar_album/<int:album_id>/', views.eliminar_album, name='Eliminar Album'),
    path('eliminar_cancion/<int:cancion_id>/', views.eliminar_cancion, name='Eliminar Cancion'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='Eliminar Usuario'),
    path('eliminar_compra/<int:compra_id>/', views.eliminar_compra, name='Eliminar Compra'),
    
]


