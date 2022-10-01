from django.contrib import admin
from django.urls import path
from core import views
from external_integartion.views import ExternalAPIView
urlpatterns = [
    path('test/', ExternalAPIView.as_view(), name="test")
]
