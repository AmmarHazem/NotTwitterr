from channels.consumer import AsyncConsumer, SyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404
import json
from tweets.models import Tweet
from .models import LikeNotification


class NotificationConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.group_name = f'user_{self.scope["user"].username}'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )

        self.send({
            'type' : 'websocket.accept',
        })
        print(f'CONNECTED: {event}')

    def receive_data(self, event):
        data = event.get('text')
        if data is not None:
            data = json.loads(data)
            return data

    def websocket_receive(self, event):
        data = self.receive_data(event)
        print(f'RECEIVED: {data}')
        # create like notification obj
        notif_obj = self.notification_create(data)
        async_to_sync(self.channel_layer.group_send)(
            f'user_{notif_obj.destination.username}',
            {
                'type' : 'send_notif',
                'text' : notif_obj.content
            }
        )

    def send_notif(self, event):
        self.send({
            'type' : 'websocket.send',
            'text' : event['text']
        })

    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
        )
        print(f'DISCONNECTED: {event}')

    def notification_create(self, data):
        user = self.scope['user']
        tweet = get_object_or_404(Tweet, id = data.get('tweetId'))
        other_user = tweet.user
        like_notif = LikeNotification(source = user, destination = other_user, tweet = tweet)
        like_notif.content = f'{user} liked your tweet.'
        like_notif.save()
        return like_notif
