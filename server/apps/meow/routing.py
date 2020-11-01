from django.urls import path
from .consumers import JokesConsumer
websocket_urlpatterns = [
    path("ws/meowfacts/", JokesConsumer),
    # path("ws/table/", TableCustomer),
]
