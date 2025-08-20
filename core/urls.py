from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rol_usuario.views import RolUsuarioViewSet

router = DefaultRouter()
router.register(r'roles', RolUsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
