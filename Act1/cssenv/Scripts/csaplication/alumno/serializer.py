from rest_framework import serializers
from alumno.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__')
    
 