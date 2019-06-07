from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_calendar_index, name='daily_calendar_index'),
    path('<int:pk>/', views.daily_calendar_detail, name='daily_calendar_detail'),
]
