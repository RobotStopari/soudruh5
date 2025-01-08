from ..models import *

def ResetPlayer(player): # vyresetuj data hráče
    player.joined_room_at = None
    
    player.pindex = 0
    player.money = 0
    player.category = '1-BEZ'
    player.marcs = 0
    
    player.looks_like_stalin = False
    player.propustka = False
    player.proverka = False
    player.nuzky = False
    player.vesta = False
    player.plan_zaminovani = False
    
    player.active = True
    player.on_move = False
    player.skipped = 0
    player.wait_moves = 0
    
    player.save()
    
    
def UpdateNumberOfPlayers(room): # nastav počet hráčů v místnosti na reálný počet hráčů v místnosti
    room.number_of_players = Player.objects.filter(room=room).count()
    room.save()
    
    
def NextPlayerOnMove(num_in_room, last_player): # odpověz, jaký hráč je v pořadí na tahu
    if last_player < num_in_room:
        return last_player + 1
    else:
        return 1
    
def ChangeTurn(player): # změň hráče na tahu na dalšího
    room = player.room
    
    CheckPlayerOnMoveForErrors(room) # zkontroluj správnou synchronizaci hráčů na tahu (zajistí, že na tahu je a bude jen jeden hráč)
    
    player.on_move = False
    player.save() # hráč na tahu už není na tahu
    
    players_in_room = Player.objects.filter(room=room).order_by('joined_room_at') # kolik je hráčů v místnosti
    room.actual_player = NextPlayerOnMove(players_in_room.count(), room.actual_player) 
    room.save() # hráč na tahu podle místnosti je další hráč v pořadí podle funkce
    
    next_player = players_in_room[room.actual_player - 1]
    next_player.on_move = True
    next_player.save() # hráč podle místnosti byl označen za na tahu
    
def CheckPlayerOnMoveForErrors(room): # porovná, kdo je opravdu na tahu a kdo má podle místnosti být na tahu
    UpdateNumberOfPlayers(room) # nastaví room_players na počet hráčů v místnosti
    
    room_players = Player.objects.filter(room=room).order_by('joined_room_at') # kolik je hráčů v místnosti
    player_on_move = room_players.filter(on_move=True) # kolik je hráčů v místnosti na tahu
    actual_player = room.actual_player # kdo je podle místnosti aktuálně na tahu
    
    print(player_on_move)
    
    if player_on_move.count() > 1: # pokud je na tahu víc než jeden hráč najednou
        for player in room_players: # každému hráči je řečeno, že není na tahu
            player.on_move = False
            player.save()
        print('Na tahu bylo najednou více, než jeden hráč.') # spustí následující if (na tahu je 0 hráčů)
    
    if player_on_move.count() < 1: # pokud nikdo není na tahu
        first_in_room = room_players.first()
        first_in_room.on_move = True
        first_in_room.save()
        print('Nikdo nebyl na tahu. Nyní je na tahu první hráč v místnosti.') # prvního hráče v místnosti nastaví na na tahu
    
    if not (1 <= room.actual_player <= room.number_of_players): # pokud aktuální hráč podle místnosti není v rozmezí počtu hráčů v místnosti
        room.actual_player = room.number_of_players
        room.save()
        actual_player = room.actual_player
        print('Aktuální hráč podle místnosti není v rozmezí počtu hráčů v místnosti. Nyní je na tahu poslední hráč v místnosti.') # nastav posledního hráče v místnosti na na tahu
        
    player_on_move = room_players.filter(on_move=True)
    room_players_list = list(room_players) # převede hráče v místnosti na seznam
    player_on_move_position = room_players_list.index(player_on_move.first()) + 1 # uloží pozici hráče, který je aktuálně na tahu
    
    if actual_player != player_on_move_position: # pokud hráč na tahu podle místnosti není stejný, jako reálný hráč na tahu
        old = player_on_move.first()
        old.on_move = False
        old.save() # reálný hráč na tahu už není na tahu
        new = room_players[actual_player - 1]
        new.on_move = True
        new.save() # na na tahu je nastaven správný hráč podle místnosti
        print('Na tahu v realitě nebyl stejný hráč, jako podle místnosti. Už není na tahu. Nyní je v realitě na tahu hráč podle místnosti.')
    
    return (print('Hráč na tahu je správně synchronizovaný.')) # vše bylo v pořádku