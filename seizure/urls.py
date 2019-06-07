from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.seizure_index, name='seizure_index'),
    path('<int:pk>/', views.seizure_detail, name='seizure_detail'),
]
