from django.db import models
from django.contrib.auth.models import User
from medication.models import Medication
from seizure.models import Seizure

# Create your models here.
class DailyCalendar(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE) 
  seizure = models.ForeignKey(Seizure, on_delete=models.CASCADE)
  medication = models.ManyToManyField(Medication)
  

  def __str__(self):
    return self.name