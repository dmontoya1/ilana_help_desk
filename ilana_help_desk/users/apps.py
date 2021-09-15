from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "ilana_help_desk.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import ilana_help_desk.users.signals  # noqa F401
        except ImportError:
            pass
