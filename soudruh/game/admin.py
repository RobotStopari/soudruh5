from django.contrib import admin
from .models import *

from django.contrib.auth.models import Group

admin.site.site_header = 'Admine, nezlob se!'
admin.site.site_title = 'Soudruh Admin'

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('account', 'id', 'room', 'category', 'pindex', 'money')
    
    readonly_fields = ('account', 'id', 'joined_room_at', 'last_notification_read', 'active', 'on_move')
    
    fieldsets = (
        (None, {
            "fields": (
                'account', 'color', 'room', 'id', 'joined_room_at', 'last_notification_read',
            ),
        }),
        ('Game Data', {
            "fields": (
                'pindex', 'category', 'money', 'marcs',
            ),
        }),
        ('Equipment', {
            "fields": (
                'looks_like_stalin', 'propustka', 'proverka', 'nuzky', 'vesta', 'plan_zaminovani',
            ),
        }),
        ('Game Status', {
            "fields": (
                'active', 'on_move', 'skipped', 'wait_moves',
            ),
        }),
    )
    
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'id', 'actual_player',)
    
    readonly_fields = ('id', 'number_of_players')
    
    fieldsets = (
        (None, {
            "fields": (
                'room_name', 'id', 'actual_player', 'number_of_players',
            ),
        }),
        ('Game', {
            "fields": (
                'game_starting_money',
            ),
        }),
    )
    
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'type', 'reciever', 'room',)
    readonly_fields = ('id', 'created_at',)
    
    
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('message', 'room',)
    readonly_fields = ('id', 'created_at',)
    

admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Postih)
admin.site.register(Vylepseni)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(History, HistoryAdmin)


admin.site.unregister(Group)