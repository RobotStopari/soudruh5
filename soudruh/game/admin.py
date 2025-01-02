from django.contrib import admin
from .models import *

from django.contrib.auth.models import Group

admin.site.site_header = 'Admine, nezlob se!'
admin.site.site_title = 'Soudruh Admin'

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('account', 'id', 'room', 'category', 'pindex', 'money')
    
    readonly_fields = ('id',)
    
    fieldsets = (
        (None, {
            "fields": (
                'account', 'color', 'room', 'id',
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
    
    readonly_fields = ('id',)
    
    fieldsets = (
        (None, {
            "fields": (
                'room_name', 'id', 'actual_player',
            ),
        }),
        ('Game', {
            "fields": (
                'game_starting_money',
            ),
        }),
    )
    
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('header', 'id', 'player',)
    readonly_fields = ('id',)
    

admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Postih)
admin.site.register(Vylepseni)
admin.site.register(Message, MessageAdmin)

admin.site.unregister(Group)