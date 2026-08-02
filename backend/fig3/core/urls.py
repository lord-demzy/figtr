"""URL configuration for the FIG3 Core application."""

from django.urls import path

from fig3.core.views import health_check

urlpatterns = [
    path("health/", health_check, name="health-check"),
]
