from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuration for the FIG3 Core application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "fig3.core"
    label = "fig3_core"
    verbose_name = "FIG3 Core"