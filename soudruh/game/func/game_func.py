from ..models import *

from random import randint

SAD = [7, 16, 21, 33, 45, 55, 70, 73, 81, 101, 120, 145, 165, 170, 205, 254, 275, 289, 305, 310, 347, 356, 394, 395, 397, 398, 399, 430, 432, 434]
HAPPY = [26, 64, 91, 106, 113, 129, 142, 148, 156, 178, 188, 217, 234, 248, 264, 268, 295, 322, 336, 362, 370, 384, 410, 422]
NO_PROVS = [132, 134, 136, 158, 160, 162]
PROVS = [131, 133, 135, 159, 161, 163]
MONEY_PLACES = [15, 29, 43, 56, 72, 86, 100, 115, 128, 143, 172, 186, 201, 215, 230, 244, 259, 273, 288, 303, 317, 332, 346, 361, 376, 390, 405, 419]
MONEY_PLACES_VALUES = [700, 750, 800, 850, 900, 950, 1000, 2500, 3500, 5000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 28000, 32000, 40000, 46000, 50000, 100000, 100000, 100000, 100000, 100000]
    
    
def RollDice(max): # hoď kostkou
    return randint(1, max)

def Notify(type, message, player, room): # ulož do databáze zprávu
    new_notification = Notification(type=type, message=message, reciever=player, room=room)
    new_notification.save()

def AddHistoryRecord(message, type, room): # ulož do databáze history record
    new_record = History(message=message, type=type, room=room)
    new_record.save()
    
def NewNotification(message, type, reciever, room): # ulož do databáze notifikaci
    new_notification = Notification(message=message, type=type, reciever=reciever, room=room)
    new_notification.save()
    
def CheckForSpecialPlaces(pindex, player, room):
    if pindex in SAD:
        NewNotification('Je to smutné.', 'sad', player, room)
        AddHistoryRecord('Je to smutné.', 'sad', room)
    elif pindex in HAPPY:
        NewNotification('Je to veselé.', 'happy', player, room)
        AddHistoryRecord('Je to veselé.', 'happy', room)