from django.conf import settings as django_settings
SIMPLENEWS_PLUGIN_MENU_INDEX = getattr(django_settings, 'SIMPLENEWS_PLUGIN_MENU_INDEX', 1)
