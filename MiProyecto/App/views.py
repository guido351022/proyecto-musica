from django.shortcuts import render
from App.models import *
from .forms import Crear_Artista_forms, Crear_Genero_forms, Crear_Cancion_forms, Crear_Compra_forms, Crear_Usuario_forms, Crear_Album_forms
def mostrar_index(request):

    return render(request, 'App/index.html')


def mostrar_usuario(request):
    usuario = Usuario.objects.all()

    context = {'usuario': usuario}

    return render(request, 'App/Usuario.html', context= context)

def mostrar_album(request):
    album = Album.objects.all()

    context = {'album': album}

    return render(request, 'App/Album.html', context= context)

def mostrar_artista(request):

    artista = Artista.objects.all()

    context = {'artista': artista}

    return render(request, 'App/Artista.html', context= context)

def mostrar_cancion(request):
    cancion = Cancion.objects.all()

    context= {'cancion': cancion}

    return render(request, 'App/Cancion.html', context= context)

def mostrar_genero(request):
    genero= Genero.objects.all()

    context= {'genero': genero}

    return render(request, 'App/Genero.html', context= context)

def mostrar_compra(request):
    compra= Compra.objects.all()

    context= {'compra': compra}

    return render(request, 'App/Compra.html', context= context)


def crear_usuario(request):
    if request.method == 'POST':
        form = Crear_Usuario_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            usuario = Usuario(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], dni=formulario_limpio['dni'])
            usuario.save()

            return render(request, 'App/index.html')
    else:
        form = Crear_Usuario_forms()
    
    return render(request, 'App/Crear_usuario.html', {'form': Crear_Usuario_forms})


def crear_artista(request):
    if request.method == 'POST':
        form = Crear_Artista_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            artista = Artista(nombre=formulario_limpio['nombre'])
            artista.save()

            return render(request, 'App/index.html')
    else:
        form = Crear_Artista_forms()

    return render(request, 'App/Crear_Artista.html', {'form': Crear_Artista_forms})


def crear_genero(request):
    if request.method == 'POST':
        form = Crear_Genero_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            genero = Genero(nombre=formulario_limpio['nombre'])
            genero.save()

            return render(request, 'App/index.html')
    else:
        form = Crear_Genero_forms()

    return render(request, 'App/Crear_Genero.html', {'form': Crear_Genero_forms})


def crear_album(request):
    if request.method == 'POST':
        form = Crear_Album_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            album = Album(titulo=formulario_limpio['titulo'], artista=formulario_limpio['artista'], genero=formulario_limpio['genero'], fecha_lanzamiento=formulario_limpio['fecha_lanzamiento'])
            album.save()

            return render(request, 'App/index.html')
    else:
        form = Crear_Album_forms()

    return render(request, 'App/Crear_Album.html', {'form': Crear_Album_forms})


def crear_cancion(request):
    if request.method == 'POST':
        form = Crear_Cancion_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            cancion = Cancion(titulo=formulario_limpio['titulo'], album=formulario_limpio['album'])
            cancion.save()

            return render(request, 'App/index.html')
    else:
        form = Crear_Cancion_forms()

    return render(request, 'App/Crear_Cancion.html', {'form': Crear_Cancion_forms})


def crear_compra(request):
    if request.method == 'POST':
        form = Crear_Compra_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            compra = Compra(usuario=formulario_limpio['usuario'], album=formulario_limpio['album'])
            compra.save()

            return render(request, 'App/index.html')
    else:
        form = Crear_Compra_forms()

    return render(request, 'App/Crear_Compra.html', {'form': Crear_Compra_forms})



def buscar_artista(request):
    if request.GET.get('nombre_artista', False):
        nombre_artista = request.GET['nombre_artista']
        artistas = Artista.objects.filter(nombre__icontains=nombre_artista)

        return render(request, 'App/Buscar_Artista.html', {'artistas': artistas})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/Buscar_Artista.html', {'respuesta': respuesta})


def buscar_genero(request):
    if request.GET.get('nombre_genero', False):
        nombre_genero = request.GET['nombre_genero']
        generos = Genero.objects.filter(nombre__icontains=nombre_genero)

        return render(request, 'App/Buscar_Genero.html', {'generos': generos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/Buscar_Genero.html', {'respuesta': respuesta})

# Vista para buscar Album
def buscar_album(request):
    if request.GET.get('titulo_album', False):
        titulo_album = request.GET['titulo_album']
        albums = Album.objects.filter(titulo__icontains=titulo_album)

        return render(request, 'App/Buscar_Album.html', {'albums': albums})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/Buscar_Album.html', {'respuesta': respuesta})


def buscar_cancion(request):
    if request.GET.get('titulo_cancion', False):
        titulo_cancion = request.GET['titulo_cancion']
        canciones = Cancion.objects.filter(titulo__icontains=titulo_cancion)

        return render(request, 'App/Buscar_Cancion.html', {'canciones': canciones})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/Buscar_Cancion.html', {'respuesta': respuesta})


def buscar_usuario(request):
    if request.GET.get('nombre_usuario', False):
        nombre_usuario = request.GET['nombre_usuario']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre_usuario)

        return render(request, 'App/Buscar_Usuario.html', {'usuarios': usuarios})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/Buscar_Usuario.html', {'respuesta': respuesta})


def buscar_compra(request):
    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        compra = Compra.objects.filter(usuario__icontains=nombre)

        return render(request, 'App/Buscar_Compra.html', {'compra': compra})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/Buscar_Compra.html', {'respuesta': respuesta})




def actualizar_artista(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    if request.method == 'POST':
        form = Crear_Artista_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            artista.nombre = formulario_limpio['nombre']
            artista.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Artista_forms(initial={'nombre': artista.nombre})

    return render(request, 'App/Actualizar_Artista.html', {'form': Crear_Artista_forms})


def actualizar_genero(request, genero_id):
    genero = Genero.objects.get(id=genero_id)
    if request.method == 'POST':
        form = Crear_Genero_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            genero.nombre = formulario_limpio['nombre']
            genero.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Genero_forms(initial={'nombre': genero.nombre})

    return render(request, 'App/Actualizar_Genero.html', {'form': Crear_Genero_forms})


def actualizar_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = Crear_Album_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            album.titulo = formulario_limpio['titulo']
            album.artista = formulario_limpio['artista']
            album.genero = formulario_limpio['genero']
            album.fecha_lanzamiento = formulario_limpio['fecha_lanzamiento']
            album.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Album_forms(initial={
            'titulo': album.titulo,
            'artista': album.artista,
            'genero': album.genero,
            'fecha_lanzamiento': album.fecha_lanzamiento
        })

    return render(request, 'App/Actualizar_Album.html', {'form': Crear_Album_forms})


def actualizar_cancion(request, cancion_id):
    cancion = Cancion.objects.get(id=cancion_id)
    if request.method == 'POST':
        form = Crear_Cancion_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            cancion.titulo = formulario_limpio['titulo']
            cancion.album = formulario_limpio['album']
            cancion.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Cancion_forms(initial={'titulo': cancion.titulo, 'album': cancion.album})

    return render(request, 'App/Actualizar_Cancion.html', {'form': Crear_Cancion_forms})


def actualizar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = Crear_Usuario_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            usuario.nombre = formulario_limpio['nombre']
            usuario.apellido = formulario_limpio['apellido']
            usuario.dni = formulario_limpio['dni']
            usuario.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Usuario_forms(initial={
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'dni': usuario.dni
        })

    return render(request, 'App/Actualizar_Usuario.html', {'form': Crear_Usuario_forms})


def actualizar_compra(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    if request.method == 'POST':
        form = Crear_Compra_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            compra.usuario = formulario_limpio['usuario']
            compra.album = formulario_limpio['album']
            compra.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Compra_forms(initial={'usuario': compra.usuario, 'album': compra.album})

    return render(request, 'App/Actualizar_Compra.html', {'form': Crear_Compra_forms})


def eliminar_artista(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    artista.delete()
    artistas = Artista.objects.all()
    context = {'artistas': artistas}
    return render(request, 'App/index.html', context=context)


def eliminar_genero(request, genero_id):
    genero = Genero.objects.get(id=genero_id)
    genero.delete()
    generos = Genero.objects.all()
    context = {'generos': generos}
    return render(request, 'App/index.html', context=context)


def eliminar_album(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'App/index.html', context=context)


def eliminar_cancion(request, cancion_id):
    cancion = Cancion.objects.get(id=cancion_id)
    cancion.delete()
    canciones = Cancion.objects.all()
    context = {'canciones': canciones}
    return render(request, 'App/index.html', context=context)


def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'App/index.html', context=context)


def eliminar_compra(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    compra.delete()
    compras = Compra.objects.all()
    context = {'compras': compras}
    return render(request, 'App/index.html', context=context)
