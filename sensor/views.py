from django.shortcuts import render

# Create your views here.
from sensor.models import Temperature
from sensor.serializers import TempSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse


class temperature_api(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TempSerializer


def temperature(request):
    data = Temperature.objects.all()
    res = []
    res_2 = []
    res_3 = []
    res_4 = []
    if data:
        for i in data:
            tx = i.captime
            ty = i.captemperature
            res.append([tx.isoformat(), float(ty)])
        for i in data:
            tx = i.captime
            ty = i.caphumidity
            res_2.append([tx.isoformat(), float(ty)])
        for i in data:
            tx = i.captime
            ty = i.capillumination
            res_3.append([tx.isoformat(), float(ty)])
        for i in data:
            tx = i.captime
            ty = i.capsoilmoisture
            res_4.append([tx.isoformat(), float(ty)])

    return render(request, 'temperature_index.html', locals())


def get_temperature(request):
    data = Temperature.objects.all()
    res = []
    if data:
        for i in data:
            tx = i.captime
            ty = i.captemperature
            res.append({"time": tx.isoformat(), "Temperature": float(ty)})
    return JsonResponse({'s1': res})


def humidity(request):
    data = Temperature.objects.all()
    res_h = []
    if data:
        for i in data:
            tx = i.captime
            ty = i.caphumidity
            res_h.append({"time": tx.isoformat(), "Humidity": float(ty)})
    return JsonResponse({'s2': res_h})