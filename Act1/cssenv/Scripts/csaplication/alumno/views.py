from django.shortcuts import render
#------------Librerias------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# -------------MODELOS--------------
from alumno.models import Alumno
# ------------SERIALIZERS-----------
from alumno.serializer import AlumnoSerializer
# Create your views here.




class AlumnoList(APIView):
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete=False)
        serializer = AlumnoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = AlumnoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()#lo guarda
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)

    def put(self,request, pk,format = None):
        alumno = Alumno.objects.get(pk=pk)
        # Alumno.objects.filter(pk=pk).update(edited='True')
        # alumno.edited = "True"
        # obj.save()
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)