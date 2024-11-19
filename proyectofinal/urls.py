"""
URL configuration for proyectofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app_inicio import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_inicio.urls')),
    path('acerca/', views.acerca, name='acerca'),
    path('index/', views.index, name='index'),
    path('juego/', views.juego, name='juego'),
    path('nombre/', views.nombre, name='nombre'),
    path('basura/', views.basura, name='basura'),
    
    path('guardar_puntaje/', views.guardar_puntaje, name='guardar_puntaje'),  # Ruta para guardar puntaje
    path('puntajes/', views.ver_puntajes, name='ver_puntajes'),  # Página de puntajes
  
    
   
]