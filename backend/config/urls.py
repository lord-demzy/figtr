"""
URL configuration for the FIGTR project.

Routes:
- ``/admin/`` — Django admin.
- ``/api/`` — FIG3 Core API (health check, platform endpoints).
- ``/api/edu/`` — FIG3 Edu API (education-specific endpoints, future).
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("fig3.core.urls")),
    # FIG3 Edu endpoints will be added here in a future phase:
    # path("api/edu/", include("fig3.edu.urls")),
]
