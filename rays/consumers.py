from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer
import json


class RaysConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'TestRoom'
        self.room_group_name = 'TestGroup'

        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )

        self.accept()
        self.send(text_data=json.dumps({'status': 'connected'}))

    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, close_code):
        pass
