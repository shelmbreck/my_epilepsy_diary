from django.shortcuts import render
from django.http import HttpResponse
from .models import Seizure
from .serializers import SeizureSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def seizure_index(request):
  if request.method == 'GET':
    seizures = Seizure.objects.all()
    serializer = SeizureSerializer(seizures, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = SeizureSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return  Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def seizure_detail(request, pk):
    seizure = Seizure.objects.get(pk=pk)

    if request.method == 'GET':
      serializer = SeizureSerializer(seizure)
      return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
      serializer = SeizureSerializer(seizure, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
      print("in here")
      seizure.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

