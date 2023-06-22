from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo

# Create your views here.

def index(request):
    return render(request,'index.html')



def index(request):
    return render(request,'index.html', {
    'titulo':'Inicio',
    'mensaje':'Proyecto web con DJango (Desde el View)'
})



def index(request):
    return render(request,'index.html', {
    'titulo':'Inicio',
})


def index(request):
    cursos = ["Introducción a la Programación", "Bases de Datos", "Diseño de Interfaces de Usuario", "Algoritmos y Estructuras de Datos", "Redes de Computadoras", "Inteligencia Artificial", "Desarrollo Web"]

    return render(request,'index.html', {
'titulo':'Inicio',
'mensaje':'Proyecto Web Con DJango',
'cursos': cursos
})

