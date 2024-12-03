from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('create-room/', views.createRoom, name='create_room'),
    path('room/<str:pk>/', views.room, name='room'),
    path('join-room/', views.join_room, name='join_room')
]

