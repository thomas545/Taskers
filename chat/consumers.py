# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Chat

class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['pk']
        self.chat_room_name = Chat.objects.get(pk=self.chat_id).room_name
        self.room_group_name = 'chat_%s' % self.chat_room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def chat_message(self, event):
        chat_id = event['chat']
        sender_username = event['sender']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'chat_id': chat_id,
            'sender_username': sender_username,
            'message': message
        }))