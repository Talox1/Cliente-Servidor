
#------------Librerias------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# ---------------------Modelos----------------
from  Administrador.models import Admin  
# ------------------Serializers------------------
from  Administrador.serializers import AdminSerializer
# ---------------------Librerias Externas----------------
# import json



class AdministradorList(APIView):
# Metodo para splicitar la informacion
   def get(self, request, format=None):
      queryset = Admin.objects.filter(delete = False)
      serializer = AdminSerializer(queryset, many = True)
      return Response(serializer.data)

# Metodo para crear nuevo registro
   def post(self, request, format = None):
      serializer = AdminSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()#lo guarda
         datas = serializer.data
         return Response(datas, status = status.HTTP_201_CREATED)

   # def put(self, request, format = None):
