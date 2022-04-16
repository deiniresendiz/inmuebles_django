from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Emperesa

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificacion
        fields = '__all__'

class EdificacionSerializer(serializers.ModelSerializer):
    comnetarios = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Edificacion
        fields = '__all__'

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    edificacionList = EdificacionSerializer(many=True, read_only=True)
    # edificacionList = serializers.StringRelatedField(many=True,)
    # edificacionList = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #edificacionList = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='edificacion-detalle')
    class Meta:
        model = Emperesa
        fields = '__all__'



    # def get_longitud_direccion(self, obj):
    #     cantidad_caracteres = len(obj.direccion)
    #     return cantidad_caracteres
    #
    # def validate(self, data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError("La direccion y el pais no pueden ser iguales")
    #     else:
    #         return data
    #
    # def validate_imagen(self, data):
    #     if len(data) > 2:
    #         raise serializers.ValidationError("La url de la imagen es muy corta")
    #     else:
    #         return data


# def column_logitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("La longitud debe ser mayor a 2")
#
# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_logitud])
#     pais = serializers.CharField()
#     decription = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.decription = validated_data.get('decription', instance.decription)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         if data['direccion']==data['paia']:
#             raise serializers.ValidationError("La direccion y el pais no pueden ser iguales")
#         else:
#             return data
#
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError("La longitud debe ser mayor a 2")
#         else:
#             return data