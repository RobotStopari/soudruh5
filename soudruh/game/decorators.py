from django.http import HttpResponse
from django.shortcuts import redirect

def user_not_auth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

def auth_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('index')
        
    return wrapper_func


def auth_user_roomless(view_func):
        
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        
        if not user.is_authenticated:
            return redirect('index')
        else:
            
            if user.player.room is None:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('room', pk=user.player.room.id)
        
    return wrapper_func


def auth_user_in_room(view_func):
        
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        user_room = user.player.room.id
        pk = kwargs['pk']
        
        if not user.is_authenticated:
            return redirect('index')
        else:
              
            if user.player.room is None:
                return redirect('home')
            else:
                
                if pk == str(user_room):
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('room', pk=user_room)
        
    return wrapper_func

def user_on_move(view_func):
        
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        user_room = user.player.room.id
        user_on_move = user.player.on_move
        
        if not user.is_authenticated:
            return redirect('index')
        else:
              
            if user.player.room is None:
                return redirect('home')
            else:
                
                if user_on_move:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('room', pk=user_room)
        
    return wrapper_func