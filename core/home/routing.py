from django.urls import path
from home.Consumer import *

webscoket_ursl = [
    path('ws/sc/',MySyncConsumer.as_asgi())
]