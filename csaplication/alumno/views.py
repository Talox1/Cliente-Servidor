from django.shortcuts import render

# Create your views here.
# -------------MODELOS--------------
from alumno.models import Alumno

# ------------SERIALIZERS-----------
from alumno.serializer import AlumnoSerializer
# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from django.http import Http404

class AlumnoList(APIView):
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete=False)
        serializer = AlumnoSerializer(queryset, many=True)
        return Response(serializer.data)