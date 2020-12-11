from django.db import models

class Contacto(models.Model):
    titulo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fono = models.IntegerField()
    mensaje = models.TextField()
    receptor = models.CharField(max_length=100, default='contacto@clavistev.cl')
    estado = models.CharField(max_length=50, default='Recepcionado')

    def __str__(self):
        return self.titulo +' '+ str(self.fono)
