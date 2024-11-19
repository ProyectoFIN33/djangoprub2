from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index4.html', {})
def about(request):
    return render(request, 'about.html')
def acerca(request):
    return render(request, 'acerca.html')

def index(request):
    return render(request, 'index.html')
def juego(request):
    return render(request,'juego.html')
def nombre(request):
    return render(request,'nombre.html')
def basura(request):
    return render(request,'basura.html')


from django.http import JsonResponse
from .models import Puntaje
import json

def guardar_puntaje(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        puntaje = request.POST.get('puntaje')
        
        # Guardar el puntaje en la base de datos
        Puntaje.objects.create(nombre=nombre, puntaje=int(puntaje))
        
        return JsonResponse({'message': 'Puntaje guardado exitosamente'})
    return JsonResponse({'message': 'Método no permitido'}, status=405)


def ver_puntajes(request):
    puntajes = Puntaje.objects.all()  # Recupera todas las puntuaciones
    return render(request, 'puntajes.html', {'puntajes': puntajes})
