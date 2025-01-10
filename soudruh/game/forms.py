from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *



class CreateUserForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_name']
        
class SelectRoomForm(ModelForm):
    class Meta:
        model = Player
        fields = ['room']
        
class LeaveRoomForm(ModelForm):
    class Meta:
        model = Player
        fields = ['room']
        
class CubeForm(ModelForm):
    class Meta:
        model = Player
        fields = []
        
class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message', 'author', 'room']