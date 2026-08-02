from django.apps import AppConfig


class EduConfig(AppConfig):
    """Configuration for the FIG3 Edu application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "fig3.edu"
    label = "fig3_edu"
    verbose_name = "FIG3 Edu"