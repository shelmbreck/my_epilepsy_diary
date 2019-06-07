from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyCalendar
from .serializers import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def daily_calendar_index(request):
  if request.method == 'GET':
    daily_calendar = DailyCalendar.objects.all()
    serializer = DailyCalendarSerializer(daily_calendar, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = DailyCalendarSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return  Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def daily_calendar_detail(request, pk):
    daily_calendar = DailyCalendar.objects.get(pk=pk)

    if request.method == 'GET':
      serializer = DailyCalendarSerializer(daily_calendar)
      return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
      serializer = DailyCalendarSerializer(daily_calendar, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
      print("in here")
      daily_calendar.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)