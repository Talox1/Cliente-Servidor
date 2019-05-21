#------------Librerias------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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

   def put(self,request, pk,format = None):
      admin = Admin.objects.get(pk=pk)
      # admin.admin_edited =True
      serializer = AdminSerializer(admin, data=request.data)
      if serializer.is_valid():
         # serializer.data.edited=True
         serializer.save()
         return Response(serializer.data)

class AdministradorDetail(APIView):
   # METODO PARA CONSULTAR ID, Y ME RETORNE SI EXISTE O NO
   def get_object(self, pk):
      try:
         return Administrador.objects.get(pk = pk)
      except Administrador.DoesNotExist:
         return "No"
   # METODO PARA CONSULTAR ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
   def get(self, request, pk, format = None):
      Id = self.get_object(pk)
      if Id!= "No":
         Id = AdminSerializer(Id)
         return Response(Id.data)
      return Response("No existe el registro")
   # METODO PARA CONSULTAR EL ID Y ACTUALIZAR LOS VALORES DE SUS CAMPOS
   def put(self, request, pk, format = None):
      Id = self.get_object(pk)
      serializer = AdminSerializer(Id, data = request.data)
      if serializer.is_valid():
         serializer.save()
         datas = serializer.data
         return Response(datas)
      return Response("Error, No hubieron cambios", status = status.HTTP_404_BAD_REQUEST)