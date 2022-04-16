from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer
from inmuebleslist_app.models import Edificacion, Emperesa

class EmpresaAV(APIView):
    def get(self, request):
        empresas = Emperesa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpresaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Emperesa.objects.get(pk=pk)
        except Emperesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            empresa = Emperesa.objects.get(pk=pk)
        except Emperesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            empresa = Emperesa.objects.get(pk=pk)
        except Emperesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EdificacionListAV(APIView):
    def get(self, request, format=None):
        inmuebles = Edificacion.objects.all()
        serializer = EdificacionSerializer(inmuebles, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EdificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetalleAV(APIView):

    def get(self, request, pk, format=None):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(edificacion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(edificacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        edificacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmuebles, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         de_serializer = InmuebleSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data, status=201)
#         else:
#             return Response(de_serializer.errors, status=400)
#
# def inmueble_detalle(request, pk):
#     if request.method == 'GET':
#         inmueble = Inmueble.objects.get(pk=pk)
#         serializer = InmuebleSerializer(inmueble)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk=pk)
#         de_serializer = InmuebleSerializer(inmueble,data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data, status=201)
#         else:
#             return Response(de_serializer.errors, status=400)
#
#     if request.method == 'DELETE':
#         inmueble = Inmueble.objects.get(pk=pk)
#         inmueble.delete()
#         return Response(status=204)





