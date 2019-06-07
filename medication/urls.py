from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.medication_index, name='medication_index'),
    path('<int:pk>/', views.medication_detail, name='medication_detail'),
]
