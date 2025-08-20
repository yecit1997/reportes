from django.db import models
import uuid

class RolUsuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Rol de Usuario'
        verbose_name_plural = 'Roles de Usuario'
        ordering = ['nombre']
