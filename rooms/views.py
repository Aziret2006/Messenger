from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

# Create your views here


@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(
                request=request, 
                template_name='room/rooms.html',
                context={'rooms': rooms} 
                 )


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room).order_by('created_date')
    
    return render(
                request=request, 
                template_name='room/room.html',
                context={'room': room, 'messages': messages} 
                 )

                