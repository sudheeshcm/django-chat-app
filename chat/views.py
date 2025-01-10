from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, room_id):
    return render(request, 'room.html')

def register_room(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room_name).exists():
        room = Room.objects.get(name=room_name)
        return redirect('room/'+str(room.id)+'?username='+username)
    else:
        room = Room.objects.create(name=room_name)
        room.save()
        return redirect('room/'+str(room.id)+'?username='+username)