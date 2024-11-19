from django.db import models

class Puntaje(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del jugador
    puntaje = models.IntegerField()  # Puntaje obtenido
   

    def __str__(self):
        return f'{self.nombre} - {self.puntaje}'
