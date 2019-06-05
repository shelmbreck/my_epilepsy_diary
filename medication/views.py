from django.shortcuts import render
from django.http import HttpResponse
from .models import Medication
from .serializers import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def medications_index(request):
  if request.method == 'GET':
    medications = Medication.objects.all()
    serializer = MedicationSerializer(seizures, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = MedicationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return  Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def medication_detail(request, pk):
    medication = Medication.objects.get(pk=pk)

    if request.method == 'GET':
      serializer = MedicationSerializer(medication)
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