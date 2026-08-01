"""URL configuration for the core application."""

from django.urls import path

from core.views import health_check

urlpatterns = [
    path("health/", health_check, name="health-check"),
]
