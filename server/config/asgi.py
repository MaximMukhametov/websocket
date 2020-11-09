"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import (
	get_default_application, ProtocolTypeRouter,
	URLRouter
	)

from apps.table.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.settings")
django.setup()
application = ProtocolTypeRouter(
    {"websocket": URLRouter(websocket_urlpatterns)}
)
