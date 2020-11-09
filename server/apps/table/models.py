from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django_fsm import FSMField, transition


class Table(models.Model):
	type = models.CharField(max_length=20, verbose_name='Type of the game')
	created_at = models.DateTimeField(auto_now_add=True,
	                                  verbose_name='Created time')
	status = FSMField(default="disable")

	@transition(field=status, source="disable", target="enable")
	def enable(self):
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
			"222", {"type": "status_socket_update",
			                  "status": "enable",
			                  "table_id": self.id,
			                  }
			)

	@transition(field=status, source="enable", target="disable")
	def disable(self):
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
			"333", {"type": "status_socket_update",
			                  "status": "disable",
			                  "table_id": self.id,
			                  }
			)
