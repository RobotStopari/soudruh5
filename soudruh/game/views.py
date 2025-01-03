from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm, RoomForm, SelectRoomForm, LeaveRoomForm, CubeForm
from .decorators import *
from .models import *
from .serializers import PlayerSerializer, MessageSerializer
from .functions import *


#   USER HANDLING - index, register, login, logout

@user_not_auth
def index(request):
    return render(request, 'game/index.html')

@user_not_auth
def registerPage(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        color = request.POST.get('color')
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            Player.objects.create(
                account=user,
                color=color,
            )
            
            messages.success(request, 'Přibyl k nám soudruh ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'game/register.html', context)


@user_not_auth
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect!')

    
    context = {}
    
    return render(request, 'game/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')



#   ROOM HANDLING - home, create room, join room

@auth_user_roomless
def home(request):
    return render(request, 'game/home.html')

@auth_user_roomless
def createRoom(request):        
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            
            room_to_join = Room.objects.last()
            player = request.user.player
            player.room = room_to_join
            player.is_room_admin = True
            
            ResetPlayer(player)
            
            player.on_move = True
            player.save()
            
            UpdateNumberOfPlayers(room_to_join)
            
            room_to_join.actual_player = 1
            room_to_join.save()
            
            return redirect('room', pk=player.room.id)
        
    context = {'form':form}
    
    return render(request, 'game/new_room_form.html', context)
    
@auth_user_roomless
def join_room(request):
    form = SelectRoomForm
    
    if request.method == 'POST':
        form = SelectRoomForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data.get('room')
            
            if room == None:
                return redirect('join_room')
            
            player = request.user.player
            player.room = room
            ResetPlayer(player)
            UpdateNumberOfPlayers(room)
            return redirect('room', pk=player.room.id)
    
    context = {'form':form}
    
    return render(request, 'game/join_room.html', context)




#   GAME - room, cube, ajax    

@auth_user_in_room
def room(request, pk):
    player = request.user.player
    room = Room.objects.get(id=pk)
    players = Player.objects.filter(room=room)
    
    form = LeaveRoomForm

    if request.method == 'POST':
            form = LeaveRoomForm(request.POST, instance=request.user.player)
            if form.is_valid():   
                
                form.save()             
                
                if players.count() < 1:
                    room.delete()
                    
                
                return redirect('home')

    context = {'room':room, 'players':players, 'player':player}
    
    return render(request, 'game/room.html', context)
    
@user_on_move
def cube(request):
    form = CubeForm
    player = request.user.player
    username = player.account.username.capitalize()
    room = player.room
        
    if request.method == 'POST':
        form = CubeForm(request.POST, instance=request.user.player)
        
        if form.is_valid():
            
            dice_roll = RollDice(6)
            player.pindex += dice_roll
            SendMessage('dice', (username + ' hodil ' + str(dice_roll) + '.'), player, room)
            
            ChangeTurn(player)
                    
    return JsonResponse({})
    
    
@auth_user
def ajax_data(request):
    room = request.user.player.room
    player = request.user.player  
    players = Player.objects.filter(room=room)
    messages = Message.objects.filter(reciever=player).filter(room=room)

    players_json = PlayerSerializer(players, many=True).data
    messages_json = MessageSerializer(messages, many=True).data

    return JsonResponse({
        'players': players_json,
        'messages': messages_json,
        'player_id': player.id,
    })
    
    