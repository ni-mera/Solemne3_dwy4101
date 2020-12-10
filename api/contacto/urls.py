from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Contacto
# Serializers define the API representation.
class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'titulo', 'nombre', 'email', 'fono',
         'mensaje', 'receptor', 'estado']

# ViewSets define the view behavior.
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', ContactoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]