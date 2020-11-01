from django.db import models
from django_fsm import FSMField, transition


class Table(models.Model):
    status = FSMField(default="disable")

    @transition(field=status, source="disable", target="enable")
    def enable(self):
        pass

    @transition(field=status, source="enable", target="disable")
    def disable(self):
        pass