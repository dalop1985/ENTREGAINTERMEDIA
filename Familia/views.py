from django.shortcuts import render
from .models import *
from django.http import *
from Familia.forms import *
# Create your views here.

def tios(request):

    tios=Tios(nombre="Jorge", apellido="Lopez", proveniente="papa", edad=55, nacimiento="1956-11-28")
    tios.save()
    edad2= str(tios.edad)
    nacimiento2= str(tios.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+tios.nombre+" "+tios.apellido+", Proveniente de: "+tios.proveniente+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)

def herm(request):

    herm=Hermanos(nombre="Joanna", apellido="Lopez", edad=40, nacimiento="1982-02-27")
    herm.save()
    edad2= str(herm.edad)
    nacimiento2= str(herm.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+herm.nombre+" "+herm.apellido+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)

def prim(request):

    prim=Primos(nombre="Diana", apellido="Navarrete", edad=38, nacimiento="1983-11-19")
    prim.save()
    edad2= str(prim.edad)
    nacimiento2= str(prim.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+prim.nombre+" "+prim.apellido+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)

def viven(request):

    viven=Viven(ciudad="Ticul", estado="Yucatán")
    viven.save()
    cadena_Texto=str("Pariente Vive en: "+viven.ciudad+", del Estado de: "+viven.estado)
    return HttpResponse(cadena_Texto)

def trab(request):

    trab=Trabajo(profesion="Administrador", titulo="Ingeniero", mail="admin@gmail.com", activo=1)
    trab.save()
    mail2=str(trab.mail)
    activo2=str(trab.activo)
    cadena_Texto=str("Pariente con Profesión de: "+trab.profesion+", con Título de: "+trab.titulo+"; el mail es: "+mail2+" y está en estatus: "+activo2)
    return HttpResponse(cadena_Texto)

def inicio(request):
    return render(request, 'Familia/inicio.html')

def Familia_tios(request):
    if request.method=="POST":
        form=FormTios(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombret=info["nombre"]
            apellidot=info["apellido"]
            provenientet=info["proveniente"]
            edadt=info["edad"]
            nacimientot=info["nacimiento"]

            tiost=Tios(nombre=nombret,apellido=apellidot,proveniente=provenientet,edad=edadt,nacimiento=nacimientot)
            tiost.save()
            return render(request, 'Familia/inicio.html')
    else:
        form=FormTios()

    return render(request, 'Familia/Familia_tios.html', {"form":form})

def Familia_hermanos(request):
    if request.method=="POST":
        form=FormHermanos(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombreh=info["nombre"]
            apellidoh=info["apellido"]
            edadh=info["edad"]
            nacimientoh=info["nacimiento"]

            hermanosh=Hermanos(nombre=nombreh,apellido=apellidoh,edad=edadh,nacimiento=nacimientoh)
            hermanosh.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormHermanos()

    return render(request, 'Familia/Familia_hermanos.html', {"form":form})


def Familia_primos(request):
    if request.method=="POST":
        form=FormPrimos(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombrep=info["nombre"]
            apellidop=info["apellido"]
            edadp=info["edad"]
            nacimientop=info["nacimiento"]

            primosp=Hermanos(nombre=nombrep,apellido=apellidop,edad=edadp,nacimiento=nacimientop)
            primosp.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormHermanos()

    return render(request, 'Familia/Familia_primos.html', {"form":form})

def Familia_lugar(request):
    if request.method=="POST":
        form=FormViven(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            ciudadv=info["ciudad"]
            estadov=info["estado"]
            
            lugarv=Viven(ciudad=ciudadv,estado=estadov)
            lugarv.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormViven()

    return render(request, 'Familia/Familia_lugar.html', {"form":form})


def Familia_trabajan(request):
    if request.method=="POST":
        form=FormTrabajan(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesiont=info["profesion"]
            titulot=info["titulo"]
            mailt=info["mail"]
            activot=info["activo"]
            
            trabajant=Trabajo(profesion=profesiont,titulo=titulot,mail=mailt,activo=activot)
            trabajant.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormTrabajan()

    return render(request, 'Familia/Familia_trabajan.html', {"form":form})

#Terminan las páginas para agregar

#Inician las páginas de búsquedas

def BFamilia_tios(request):
    return render(request, 'Familia/BFamilia_tios.html')

def BFamilia_hermanos(request):
    return render(request, 'Familia/BFamilia_hermanos.html')

def BFamilia_primos(request):
    return render(request, 'Familia/BFamilia_primos.html')

def BFamilia_lugar(request):
    return render(request, 'Familia/BFamilia_lugar.html')

def BFamilia_trabajan(request):
    return render(request, 'Familia/BFamilia_trabajan.html')

#Termina el segmento de las páginas de búsquedas

#Inicia el segmento de las páginas con resultados de las búsquedas

def Btios(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        #Tios=Tios.objects.all()
        #Tios=Tios.objects.get(nombre=nombre)
        nombres=Tios.objects.filter(nombre=nombre)
        return render(request,"Familia/RBFamilia_tios.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_tios", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

def Bhermanos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nombres=Hermanos.objects.filter(nombre=nombre)
        return render(request,"Familia/RBFamilia_hermanos.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_hermanos", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

def Bprimos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nombres=Primos.objects.filter(nombre=nombre)
        return render(request,"Familia/RBFamilia_primos.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_primos", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

def Blugar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nombres=Viven.objects.filter(ciudad=nombre)
        return render(request,"Familia/RBFamilia_lugar.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_lugar", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

def Btrabajan(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nombres=Trabajo.objects.filter(profesion=nombre)
        return render(request,"Familia/RBFamilia_trabajan.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_trabajan", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})
#Termina el segmento de las páginas con resultados de las páginas