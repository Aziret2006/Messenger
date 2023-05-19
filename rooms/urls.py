from django.urls import path

from .views import list_rooms, detail_room

urlpatterns = [
    path('', list_rooms, name='list-rooms'),
    path('<slug:slug>/', detail_room, name='detail-room')
]
