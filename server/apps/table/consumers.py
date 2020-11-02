import logging

from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class StatusCustomer(AsyncJsonWebsocketConsumer):
	"""."""

	async def connect(self):
		await self.accept()
		await self.channel_layer.group_add("status_socket", self.channel_name)
		logger.info(f"Added {self.channel_name} channel to status_socket.")

	async def disconnect(self, code):
		await self.channel_layer.group_discard("status_socket",
		                                       self.channel_name)
		logger.info(f"Removed {self.channel_name} channel to status_socket.")

	async def status_socket_update(self, event):
		await self.send_json(event)
		logger.info(f"Got message {event} at {self.channel_name}.")
