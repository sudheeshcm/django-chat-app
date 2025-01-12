from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_id>', views.room, name='room'),
    path('register_room', views.register_room, name='register'),
    path('room/<str:room_id>/get_messages', views.get_messages, name='get_messages'),
    path('submit_message', views.submit_message, name='submit_message'),
    path('user/<str:user_id>', views.user, name='user'),
]
