from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

# Create your views here


@login_required
def list_rooms(request):
    rooms = Room.objects.all()
    
    return render(
                request=request, 
                template_name='room/list.html',
                context={'rooms': rooms} 
                 )


@login_required
def detail_room(request, slug):
    room = Room.objects.get(slug=slug)
    message = Message.objects.filter(room=room)
    
    return render(
                request=request, 
                template_name='room/detail.html',
                context={'room': room, 'message': message} 
                 )

                