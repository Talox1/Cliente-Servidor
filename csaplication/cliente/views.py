from django.shortcuts import render

# Create your views here.
# -------------MODELOS--------------
from cliente.models import Cliente

# ------------SERIALIZERS-----------
from cliente.serializer import ClienteSerializer
# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from django.http import Http404

class ClienteList(APIView):
    def get(self, request, format=None):
        queryset = Cliente.objects.filter(delete=False)
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)