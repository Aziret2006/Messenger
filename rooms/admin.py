from django.contrib import admin

from .models import Room, Message

# Register your models here
class AdminRoom(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    
class AdminMessage(admin.ModelAdmin):
    list_display = ['room', 'user', 'content']
    search_fields = ['content']
    

admin.site.register(Room, AdminRoom)
admin.site.register(Message, AdminMessage)