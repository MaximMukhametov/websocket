from django.shortcuts import render
from django_fsm import TransitionNotAllowed
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.table.models import Table
from apps.table.serializers import TableSerializer


def table(request):

    return render(request, "index_table.html", {})


class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    @action(detail=True)
    def enable(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        try:
            table.enable()
            table.save()
        except TransitionNotAllowed as e:
            raise ValidationError(e)
        return Response({"status": "enabled"})

    @action(detail=True)
    def disable(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        try:
            table.disable()
            table.save()
        except TransitionNotAllowed as e:
            raise ValidationError(e)
        return Response({"status": "disable"})


