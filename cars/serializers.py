from rest_framework import serializers
from .models import Marca, Carro


class MarcaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Marca
        fields = '__all__'


class CarroSerializer(serializers.ModelSerializer):

    class Meta:

        model = Carro
        fields = '__all__'


class CarroListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Carro
        fields = ['nome', 'origem', 'data_fabricacao']