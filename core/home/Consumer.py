from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import json
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("websocket is connecting ... ",event)
        print("Channel Layer ..", self.channel_layer) #get default channel layer
        print("Channel Name ...",self.channel_name) #get channel name

        # Add a channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)(
            'programmers', #group name
            self.channel_name
        )
        self.send({
            'type' : 'websocket.accept',
        })

    def websocket_receive(self,event):
        print("Receiving data from client ... ",event['text'])
        print("Message received from clinet is in form of ... ",type(event['text']))
        async_to_sync(self.channel_layer.group_send)(
            'programmers',
            {
                'type':'chat.message',
                'message':event['text']
            }
        )

    def chat_message(self, event):
        print('Event ...',event)
        print('Actual data ... ',event['message'])
        print('type of actual data', type(event['message']))
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
        
    def websocket_disconnect(self,event):
        print("Disconnecting from client ... ",event)
        async_to_sync(self.channel_layer.group_discard)(
            'programmers', 
            self.channel_name
        )
        raise(StopConsumer)