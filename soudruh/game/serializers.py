from rest_framework import serializers
from .models import Player, Message

class PlayerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='account.username')
    email = serializers.CharField(source='account.email')

    class Meta:
        model = Player
        fields = ['id', 'name', 'email', 'color', 'pindex', 'money', 'category', 'on_move']
        
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'message', 'type', 'reciever', 'room', 'created_at']
        

