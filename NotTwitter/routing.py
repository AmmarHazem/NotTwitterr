from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from notifications.consumers import NotificationConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket' : AuthMiddlewareStack(
        URLRouter([
            url(r'^', NotificationConsumer),
        ])
    ),
})
