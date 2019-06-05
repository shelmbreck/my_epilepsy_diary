from rest_framework import serializers
from .models import Medication

class MedicationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Medication
    field = ('id', 'name', 'brand', 'dosage', 'user')