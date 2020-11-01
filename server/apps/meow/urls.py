from django.urls import path

from apps.meow.views import start_task, table

urlpatterns = [
    path("", start_task, name="run_task"),
    path("status/", table, name="table"),
]
