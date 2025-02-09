from django.contrib import admin
from .models import *

from django.contrib.auth.models import Group

admin.site.site_header = 'Admine, nezlob se!'
admin.site.site_title = 'Soudruh Admin'

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('account', 'id', 'room', 'category', 'pindex', 'money')
    
    readonly_fields = ('account', 'id', 'joined_room_at', 'last_notification_read', 'active')
    
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
    
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'author', 'room',)
    readonly_fields = ('id', 'created_at',)
    
class EffectAdmin(admin.ModelAdmin):
    list_display = ('type', 'category', 'notification_message')
    
    fieldsets = (
        ('Settings', {
            "fields": (
                'type', 'category',
            ),
        }),
        ('Messages', {
            "fields": (
                'notification_message', 'history_record_message_p1', 'history_record_message_p2',
            ),
        }),
        ('Go To', {
            "fields": (
                'go_to_vezeni', 'go_to_blazinec', 'go_to_start',
            ),
        }),
        ('Basics', {
            "fields": (
                'pindex_change_by', 'pindex_set_to', 'money_change_by', 'wait_moves_set_to',
            ),
        }),
        ('Equipment', {
            "fields": (
                'give_stalin', 'give_propustka', 'give_proverka', 'give_nuzky', 'give_vesta', 'give_plan_zaminovani',
            ),
        }),
        ('Other Players', {
            "fields": (
                'give_everybody', 'remove_from_everybody', 'money_change_by_per_player',
            ),
        }),
        ('If stalin', {
            "fields": (
                'money_change_by_if_stalin', 'notification_message_if_stalin', 'history_record_message_p1_if_stalin', 'history_record_message_p2_if_stalin',
            ),
            'description': 'Pokud jsou tato pole vyplněná a pokud hráč vypadá jako Stalin, přepíší money_change_by, notifikace a history_record zprávy ty výše uvedené. Pokud jako Stalin nevypadá, využíjí se ty původní. Je tedy potřeba vyplnit oboje.'
        }),
    )

admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Effect, EffectAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)

admin.site.unregister(Group)