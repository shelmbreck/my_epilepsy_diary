from rest_framework import serializers
from .models import DailyCalendar

class DailyCalendarSerializer(serializers.ModelSerializer):
  class Meta:
    model = DailyCalendar
    field = ('id', 'seizure', 'medication')