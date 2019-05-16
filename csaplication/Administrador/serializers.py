# ------------Librerias-----------
from rest_framework import routers, serializers, viewsets
# -------------Modelos-------------
   # |Nombre de la ap              Nombre del modelo
from  Administrador.models import Admin  

class AdminSerializer(serializers.ModelSerializer):
   class Meta:
      model = Admin
      fields = ('__all__')