from django.test import TestCase
from django.contrib.auth.models import User
from .models import Plan

# Create your tests here.
class PlanesTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(
            name = "Plan XXL",
            description = "Plan de Prueba",
            image = "",
            price = 5990
        )
        Plan.objects.create(
            name = "Plan XXS",
            description = "Plan de Prueba",
            image = "",
            price = 1000
        )
        Plan.objects.create(
            name = "Plan O",
            description = "Testing Plan",
            image = "",
            price = 29990
        )

    #Valida precio de plan creado XXL
    def test_valida_Precio(self):
        plan = Plan.objects.get(name="Plan XXL")
        self.assertEqual(plan.price, 5990)

    #Valida precio de plan creado O
    def test_valida_Precio2(self):
        plan = Plan.objects.get(name="Plan O")
        self.assertEqual(plan.price, 29990)

    #Cuenta cantidad de planes creados en test
    def test_count_planes(self):
        planes = Plan.objects.all()
        self.assertEqual(planes.count(), 3)
    
    def test_descuento(self):
        plan = Plan.objects.get(name="Plan O")
        self.assertEqual(plan.generarDescuento(), 0.6)

    def test_precio_final(self):
        plan = Plan.objects.get(name="Plan O")
        self.assertEqual(plan.calcularPrecioFinal(), 11996)