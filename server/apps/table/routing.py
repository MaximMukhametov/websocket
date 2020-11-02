from django.urls import path

from apps.table.consumers import StatusCustomer

websocket_urlpatterns = [
    path("ws/connect/", StatusCustomer),
]
