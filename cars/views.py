from rest_framework import viewsets, mixins
from .models import Marca, Carro
from .serializers import MarcaSerializer, CarroSerializer, CarroListSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()


class CarroViewSet(viewsets.ModelViewSet):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CarroListSerializer 
        else:
            return CarroSerializer