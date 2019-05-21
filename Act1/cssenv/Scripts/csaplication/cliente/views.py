
#------------Librerias------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.
# -------------MODELOS--------------
from cliente.models import Cliente

# ------------SERIALIZERS-----------
from cliente.serializer import ClienteSerializer
# Create your views here.



class ClienteList(APIView):
    def get(self, request, format=None):
        queryset = Cliente.objects.filter(delete=False)
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()#lo guarda
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)

    def put(self,request, pk,format = None):
        cliente = Cliente.objects.get(pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)