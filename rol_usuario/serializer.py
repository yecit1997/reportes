from rest_framework import serializers
from .models import RolUsuario

class RolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolUsuario
        fields = '__all__'