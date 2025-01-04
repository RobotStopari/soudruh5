from ..models import *

from random import randint
    
    
def RollDice(max): # hoď kostkou
    return randint(1, max)

def Notify(type, message, player, room): # ulož do databáze zprávu
    new_notification = Notification(type=type, message=message, reciever=player, room=room)
    new_notification.save()

def AddHistoryRecord(message, room): # ulož do databáze history record
    new_record = History(message=message, room=room)
    new_record.save()