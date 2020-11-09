import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class StatusCustomer(AsyncJsonWebsocketConsumer):
	"""."""

	async def connect(self):
		await self.accept()
		stream = self.scope["url_route"]["kwargs"]["stream"]
		logger.info(self.scope.items())
		await self.channel_layer.group_add(stream, self.channel_name)
		logger.info(f"Added {self.channel_name} channel to channel layer:{self.channel_layer} status_socket.")

	async def disconnect(self, code):
		stream = self.scope["url_route"]["kwargs"]["stream"]

		await self.channel_layer.group_discard(stream,
		                                       self.channel_name)
		logger.info(f"Removed {self.channel_name} channel to status_socket.")

	async def status_socket_update(self, event):
		await self.send_json(event)
		logger.info(f"Got message {event} at {self.channel_name}.")
