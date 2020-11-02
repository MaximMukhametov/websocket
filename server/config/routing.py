from channels.routing import ProtocolTypeRouter, URLRouter
from apps.table.routing import websocket_urlpatterns

# Channels routers only work on the scope level, not on the level of individual
# events, which means you can only have one consumer for any given connection.
# Routing is to work out what single consumer to give a connection, not how to
# spread events from one connection across multiple consumers.
application = ProtocolTypeRouter(
    {"websocket": URLRouter(websocket_urlpatterns)}
)
