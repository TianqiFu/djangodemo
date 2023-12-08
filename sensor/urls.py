from django.urls import re_path as url
from sensor import views


urlpatterns = [
    url(r'^$', views.temperature, name='sensor.temperature'),
    url(r'^temperature_api', views.temperature_api.as_view(), name='sensor.temperature_api'),
    url(r'^get_temperature', views.get_temperature, name='sensor.get_temperature'),
    url(r'^humidity', views.humidity, name='sensor.humidity')
]