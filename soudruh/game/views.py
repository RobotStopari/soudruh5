from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, RoomForm
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
                player.save()
                
                return redirect('room', pk=player.room.id)
        
        
        context = {'form':form}
        
        return render(request, 'game/new_room_form.html', context)
    
    else:
        return redirect('room', pk=pl_room.id)
    

@login_required(login_url='index')
def room(request, pk):
    pl_room = request.user.player.room
    room = Room.objects.get(id=pk)
    
    if pl_room is not None:
        if pl_room == room:
        
            context = {'room':room}
            return render(request, 'game/room.html', context)
        
        else:
            return redirect('room', pk=pl_room.id)
    
    else:
        return redirect('home')