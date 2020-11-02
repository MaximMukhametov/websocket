from django.urls import path, include
from rest_framework import routers

from apps.table.views import table, TableViewSet

router = routers.SimpleRouter()
router.register(r'table', TableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
