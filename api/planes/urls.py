from django.urls import path, include
from .models import Plan
from rest_framework import routers, serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

#Encargado de serializar los datos que llegan
class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['id','name', 'description', 'price', 'image']

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    serializer_class = PlanSerializer
    filterset_fields = ['id','name']
    search_fields = ['id','name']

router = routers.DefaultRouter()
router.register(r'', PlanViewSet)

urlpatterns = [
    path('', include(router.urls))
]