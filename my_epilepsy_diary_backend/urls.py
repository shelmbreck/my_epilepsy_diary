"""my_epilepsy_diary_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seizure/', include('seizure.urls')),
    path('medication/', include('medication.urls')),
    path('dailycalendar/', include('daily_calendar.urls')),
    # path('seizure/', views.seizure_index, name='seizure_index'),
    # path('seizure/<int:pk>/', views.seizure_detail, name='seizure_detail'),
    # path('medication/', views.medication_index, name='medication_index'),
    # path('medication/<int:pk>/', views.medication_detail, name='medication_detail'),
#     path('dailycalendar/', views.daily_calendar_index, name='daily_calendar_index'),
#     path('dailycalendar/<int:pk>/', views.daily_calendar_detail, name='daily_calendar_detail')
]
