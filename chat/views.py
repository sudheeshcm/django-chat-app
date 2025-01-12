from django.shortcuts import render, redirect
from .models import Room, Message, User
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, room_id):
    room_details = Room.objects.get(id=int(room_id))
    user_id = request.GET.get('user')
    context = {
        'room_id': room_details.id,
        'room_details': room_details,
        'user_id': user_id
    }
    return render(request, 'room.html', context)

def register_room(request):
    room_name = request.POST['room_name']
    username = request.POST['username']
    gender = request.POST['gender']

    if User.objects.filter(name=username).exists():
        user = User.objects.get(name=username)
    else:
        user = User.objects.create(name=username, gender=gender)
        user.save()

    if Room.objects.filter(name=room_name).exists():
        room = Room.objects.get(name=room_name)
        return redirect('room/'+str(room.id)+'?user='+str(user.id))
    else:
        room = Room.objects.create(name=room_name)
        room.save()
        return redirect('room/'+str(room.id)+'?user='+str(user.id))

def get_messages(request, room_id):
    messages = Message.objects.filter(room_id=int(room_id))
    return JsonResponse({'messages': list(messages.values())})

def submit_message(request):
    room_id = request.POST['room_id']
    user_id = request.POST['user_id']
    message = request.POST['message']

    user = User.objects.get(id=int(user_id))
    new_message = Message.objects.create(room_id=int(room_id), user_id=user_id,text=message)
    new_message.save()
    return HttpResponse({'new_message', new_message})

def user(request, user_id):
    user = User.objects.filter(id=int(user_id)).values()[0]
    return JsonResponse(user)