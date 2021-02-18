from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'engine_size', 'fuel_type')
