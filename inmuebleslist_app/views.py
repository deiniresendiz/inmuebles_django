# from django.http import JsonResponse
# from django.shortcuts import render
# from inmuebleslist_app.models import Inmueble
#
# # Create your views here.
# def inmueble_list(request):
#     inmueble = Inmueble.objects.all()
#     data = {"inmuebles": list(inmueble),}
#
#     return JsonResponse(data)
#
# def inmueble_detalle(request, pk):
#     inmueble = Inmueble.objects.get(pk=pk)
#     data = {
#         "direccion": inmueble.direccion,
#         "pais": inmueble.pais,
#         "imagen": inmueble.imagen,
#         "activo": inmueble.activo,
#         "description": inmueble.description,
#     }
#
#     return JsonResponse(data)

