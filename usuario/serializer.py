from rest_framework import serializers
from usuario.models import Usuario
from rol_usuario.models import RolUsuario


class UsuarioSerializer(serializers.ModelSerializer):
    rol = serializers.PrimaryKeyRelatedField(
        queryset=RolUsuario.objects.all(),  # Importante: Define el queryset para la validación
        allow_null=True,  # Si el campo 'rol' en Usuario puede ser null (como en tu modelo)
        required=False,  # Si el campo 'rol' no es obligatorio al crear/actualizar (como en tu modelo)
    )
    nombre_rol = serializers.CharField(source="rol.nombre", read_only=True)

    class Meta:
        model = Usuario
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "telefono",
            "password",
            "rol",
            "nombre_rol",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Creamos el metodo CREATE para manejar el password hasheado correctamente al crear/actualizar usuarios.
        """
        password = validated_data.pop("password", None)
        user = Usuario.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
