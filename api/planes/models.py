from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=1)
    image = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    '''
    def __str1__(self):
        return self.description
    def __str2__(self):
        return self.image
    def contratarLineas(self, numeroLineas):
        return self.price * numeroLineas
    '''
    def generarDescuento(self):
        if(self.price <= 10000):
            return 0.05
        if(self.price <= 11000):
            return 0.1
        if(self.price <= 13000):
            return 0.2
        if(self.price <= 15000):
            return 0.4
        if(self.price <= 20000):
            return 0.5
        return 0.6
        
    def calcularPrecioFinal(self):
        return self.price * (1.0-self.generarDescuento())            