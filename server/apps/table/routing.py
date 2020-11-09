from django.urls import path, re_path

from apps.table.consumers import StatusCustomer

websocket_urlpatterns = [
    re_path(r"^ws/(?P<stream>\w+)/$", StatusCustomer),
]
