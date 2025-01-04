from ..models import Player, Message

from random import randint
    
    
def RollDice(max): # hoď kostkou
    return randint(1, max)

def SendMessage(type, message, player, room): # ulož do databáze zprávu
    new_message = Message(type=type, message=message, reciever=player, room=room)
    new_message.save()
