from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_id>', views.room, name='room'),
    path('register_room', views.register_room, name='register'),
]
