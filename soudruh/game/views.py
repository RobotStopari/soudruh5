from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from random import randint

from .forms import CreateUserForm, RoomForm, SelectRoomForm, LeaveRoomForm, CubeForm
from .decorators import unauthenticated_user
from .models import *

@unauthenticated_user
def index(request):
    return render(request, 'game/index.html')

@login_required(login_url='index')
def home(request):
    
    pl_room = request.user.player.room
    
    if pl_room is None:
        
            return render(request, 'game/home.html')
        
    else:
        
        return redirect('room', pk=pl_room.id)

@unauthenticated_user
def registerPage(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            Player.objects.create(
                account=user,
            )
            
            messages.success(request, 'Přibyl k nám soudruh ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'game/register.html', context)


@unauthenticated_user
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

@login_required(login_url='index')
def createRoom(request):
    pl_room = request.user.player.room
    
    if pl_room is None:
        
        form = RoomForm()
        if request.method == 'POST':
            form = RoomForm(request.POST)
            if form.is_valid():
                form.save()
                
                room_to_join = Room.objects.last()
                player = request.user.player
                player.room = room_to_join
                player.is_room_admin = True
                player.save()
                
                return redirect('room', pk=player.room.id)
        
        
        context = {'form':form}
        
        return render(request, 'game/new_room_form.html', context)
    
    else:
        return redirect('room', pk=pl_room.id)
    

@login_required(login_url='index')
def room(request, pk):
    player = request.user.player
    pl_room = player.room
    room = Room.objects.get(id=pk)
    players = Player.objects.filter(room=room)
    
    if pl_room is not None:
        if pl_room == room:
            
            form = LeaveRoomForm
        
            if request.method == 'POST':
                    form = LeaveRoomForm(request.POST, instance=request.user.player)
                    if form.is_valid():
                        form.save()
                        
                        return redirect('home')
        
            context = {'room':room, 'players':players, 'player':player}
            return render(request, 'game/room.html', context)
        
        else:
            return redirect('room', pk=pl_room.id)
    
    else:
        return redirect('home')
    
@login_required(login_url='index')
def cube(request):
    form = CubeForm
    player = request.user.player
    
    if player.on_move:
        
        if request.method == 'POST':
            form = CubeForm(request.POST, instance=request.user.player)
            if form.is_valid():
                cube_roll = randint(1, 6)
                print(cube_roll)
                player.pindex += cube_roll
                player.on_move = False
                player.save()
                    
    return redirect('room',  pk=player.room.id)
    
@login_required(login_url='index')    
def join_room(request):
    pl_room = request.user.player.room
    
    if pl_room is None:
    
        form = SelectRoomForm
        
        if request.method == 'POST':
                form = SelectRoomForm(request.POST)
                if form.is_valid():
                    
                    
                    room = form.cleaned_data.get('room')
                    player = request.user.player
                    player.room = room
                    player.save()
                    return redirect('room', pk=player.room.id)
        
        context = {'form':form}
        
        return render(request, 'game/join_room.html', context)

    else:
        return redirect('room', pk=pl_room.id)
    
    
@login_required(login_url='index')    
def ajax_players(request):
    room = request.user.player.room
    player = request.user.player
    
    if room is not None:
        players = Player.objects.filter(room=room)
        
        players_json = [
            {
                'id':p.id,
                'name':p.account.username,
                'color':p.color,
                'pindex':p.pindex,
                'money':p.money,
                'category':p.category,
                'on_move':p.on_move,
                
            } for p in players]
    
    else:
        players_json = {}
    
    return JsonResponse({
        'players': players_json,
        'player_id': player.id,
    })
    
    