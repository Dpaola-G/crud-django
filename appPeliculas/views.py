from django.shortcuts import render
from django.db import Error
from appPeliculas.models import Genero,Pelicula
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.

def inicio (request):
    return render(request, "inicio.html")

def vistaAgregarGenero(request):
    return render(request, "agregarGenero.html")

def agregarGenero (request):
    try:
        nombre = request.POST ['txtNombre']
        #crear objeto de tipo nombre
        genero = Genero (genNombre=nombre)
        #salvar el objeto,lo que permite que sea
        #creado con la base de datos
        genero.save()
        mensaje="generoo Agregado correctamente"
    except Error as error:
        mensaje=str(error)
        retorno  = {"mensaje":mensaje}
        # return JsonResponse (retorno)
        return render (request, "agregarGenero.html", retorno)
    
def listarPeliculas (request):
        peliculas = Pelicula.objects.all().values ()
        retorno ={"peliculas":list (peliculas)}
        #return JsonResponse (retorno)
        return render (request, "listarPeliculas.html", retorno)
    
def vistaAgregarPelicula (request):
        generos = Genero.objects.all()
        
        retorno =
    
def agregarPelicula (request):
    try:
        codigo = request.POST['txtCodigo']
        titulo= request.POST['txtTitulo']
        protagonista= request.POST['txtProtagonista']
        duracion = int(request.POST['txtDuracion'])
        resumen= request.POST['txtResumen']
        foto= request.FILES['filefoto']
        idGenero= int(request.POST['cbGenero'])
        genero = Genero.objects.get(pk=idGenero)
        
        pelicula=Pelicula(pelCodigo=codigo,
                          pelTitulo=titulo,
                          pelProtagonista=protagonista,
                          pelDuracion=duracion,
                          pelResumen=resumen,
                          pelFoto=foto,
                          pelGenero=genero)
  
        pelicula.save()
        mensaje="pelicula agregada correctamente"
        
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje, "idPelicula": pelicula.id}
    # return JsonResponse(retorno)
    return render (request,)