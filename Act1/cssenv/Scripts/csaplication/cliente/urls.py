from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from cliente import views

urlpatterns =  [
    re_path(r'^lista/$', views.ClienteList.as_view()),
    re_path(r'^editcliente/(?P<pk>\d+)/$',views.ClienteList.as_view()),
]