from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from alumno import views



urlpatterns =  [
    re_path(r'^lista/$', views.AlumnoList.as_view()),
    re_path(r'^editalumno/(?P<pk>\d+)/$',views.AlumnoList.as_view()),
]