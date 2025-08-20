from django.shortcuts import render
from rest_framework import viewsets, status

from .models import RolUsuario
from .serializer import RolUsuarioSerializer

class RolUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RolUsuario.objects.all()
    serializer_class = RolUsuarioSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
