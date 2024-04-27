from django.shortcuts import render
import json
from rest_framework.response import Response
from rest_framework import status, permissions
from api_vehiculos.models import vehiculo
from api_vehiculos.serializer import vehiculo_serializer
from rest_framework.views import APIView

# Create your views here.
class vehiculo_api_view(APIView):
    def post(self, request, *args, **kwargs):
        data={
            'placa': request.data.get('placa'),
            'marca': request.data.get('marca'),
            'color_vehiculo': request.data.get('color'),
            'modelo': request.data.get('modelo'),
        }
        serializador=vehiculo_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data,status=status.HTTP_200_OK)
        return Response(serializador.data,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,*args,**kwargs):
        lista_vehiculos=vehiculo.objects.all()
        serializer_vehiculos=vehiculo_serializer(lista_vehiculos,many=True)
        return Response(serializer_vehiculos.data,status=status.HTTP_200_OK)
    def put(self,request,pkid):
        vehiculo_consultado=vehiculo.objects.filter(id=pkid).update(
            placa=request.data.get('placa'),
            marca=request.data.get('marca'),
            color_vehiculo=request.data.get('color'),
            modelo=request.data.get('modelo'),

        )
        return Response(vehiculo_consultado,status=status.HTTP_200_OK)
# Create your views here.
