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
from rest_framework.parsers import FileUploadParser
# ---------------------Modelos----------------
from  Profile.models import Profile  
# ------------------Serializers------------------
from  Profile.serializer import ProfileSerializer
# ---------------------Librerias Externas----------------
# import json

class ProfileList(APIView):
# Metodo para splicitar la informacion
   def get(self, request, format=None):
      queryset = Profile.objects.filter(delete = False)
      serializer = ProfileSerializer(queryset, many = True)
      return Response(serializer.data)

# Metodo para crear nuevo registro
   def post(self, request, format = None):
      serializer = ProfileSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()#lo guarda
         datas = serializer.data
         return Response(datas, status = status.HTTP_201_CREATED)

   def put(self,request, pk,format = None):
      profile = Profile.objects.get(pk=pk)
      # admin.admin_edited =True
      serializer = ProfileSerializer(admin, data=request.data)
      if serializer.is_valid():
         # serializer.data.edited=True
         serializer.save()
         return Response(serializer.data)

class ProfileDetail(APIView):
   # METODO PARA CONSULTAR ID, Y ME RETORNE SI EXISTE O NO
   def get_object(self, pk):
      try:
         return Profile.objects.get(pk = pk)
      except Profile.DoesNotExist:
         return "No"
   # METODO PARA CONSULTAR ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
   def get(self, request, pk, format = None):
      Id = self.get_object(pk)
      if Id!= "No":
         Id = ProfileSerializer(Id)
         return Response(Id.data)
      return Response("No existe el registro")
   # METODO PARA CONSULTAR EL ID Y ACTUALIZAR LOS VALORES DE SUS CAMPOS
   def put(self, request, pk, format = None):
      Id = self.get_object(pk)
      serializer = ProfileSerializer(Id, data = request.data)
      if serializer.is_valid():
         serializer.save()
         datas = serializer.data
         return Response(datas)
      return Response("Error, No hubieron cambios", status = status.HTTP_404_BAD_REQUEST)

class FileUploadView(APIView):
   parser_class = (FileUploadParser,)
   def post(self, request, *args, **kwargs):
      file_serializer = ProfileSerializer(data=request.data)
      if file_serializer.is_valid():
         file_serializer.save()
         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)      