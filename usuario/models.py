from django.db import models
from django.contrib.auth.models import AbstractUser

from rol_usuario.models import RolUsuario

class Usuario(AbstractUser):
    dni = models.CharField(max_length=20, unique=True, verbose_name='DNI')
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name='Teléfono')
    rol = models.ForeignKey(RolUsuario, on_delete=models.CASCADE, verbose_name='Rol')
