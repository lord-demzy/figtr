"""Tests for the FIG3 Core application."""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthCheckTests(APITestCase):
    """Tests for the health check endpoint."""

    def test_health_check_returns_ok(self):
        """Test that GET /api/health/ returns status ok."""
        url = reverse("health-check")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "ok"})