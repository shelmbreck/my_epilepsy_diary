from rest_framework import serializers
from .models import Seizure

class SeizureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seizure
    field = ('id', 'name', 'user')