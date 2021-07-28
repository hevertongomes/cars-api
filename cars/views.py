from rest_framework import viewsets, mixins
from django_filters import rest_framework as filters
from .models import Marca, Carro
from .serializers import MarcaSerializer, CarroSerializer, CarroListSerializer
from .pagination import SmallPagination

class MarcaFilter(filters.FilterSet):
    class Meta:
        model = Marca
        fields = {
            'nome': ['icontains'],
            'origem': ['exact'],
        }

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()
    filterset_class = MarcaFilter
    pagination_class = SmallPagination

class CarroFilter(filters.FilterSet):
    class Meta:
        model = Carro
        fields = {
            'nome': ['icontains'],
            'origem': ['exact'],
        }

class CarroViewSet(viewsets.ModelViewSet):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()
    filterset_class = CarroFilter
    pagination_class = SmallPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return CarroListSerializer 
        else:
            return CarroSerializer