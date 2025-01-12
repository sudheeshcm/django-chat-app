from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
# import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, room_id):
    room_details = Room.objects.get(id=int(room_id))
    username = request.GET.get('username')
    context = {
        'room_id': room_details.id,
        'room_details': room_details,
        'username': username
    }
    return render(request, 'room.html', context)

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

def get_messages(request, room_id):
    print('room_id', room_id)
    messages = Message.objects.filter(room_id=int(room_id))
    return JsonResponse({'messages': list(messages.values())})

def submit_message(request):
    room_id = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']
    new_message = Message.objects.create(room_id=int(room_id), username=username, text=message)
    new_message.save()
    return HttpResponse({'new_message', new_message})