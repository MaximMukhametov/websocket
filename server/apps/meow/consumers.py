from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class JokesConsumer(WebsocketConsumer):
    """
    This wraps the verbose plain-ASGI message sending and receiving into
    handling that just deals with text and binary frames.
    This class uses WebSocket consumer, which is synchronous, and so
    needs the async channel layer functions to be converted.
    """

    def connect(self):
        # Called on connection.
        async_to_sync(self.channel_layer.group_add)("meow_facts",
                                                    self.channel_name)

        # To accept the connection call:
        self.accept()

    def disconnect(self, close_code):
        # Called when the socket closes
        async_to_sync(self.channel_layer.group_discard)("meow_facts",
                                                        self.channel_name)

    def meow_facts_fact(self, event):
        self.send(text_data=event["text"])


#
# class TableCustomer():