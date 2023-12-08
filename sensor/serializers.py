from rest_framework import serializers
from sensor.models import Temperature


class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['captime','captemperature','caphumidity','capillumination','capsoilmoisture']