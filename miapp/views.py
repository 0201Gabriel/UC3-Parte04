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

