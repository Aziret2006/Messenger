from django.contrib import admin

from .models import Room

# Register your models here
class AdminRoom(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    

admin.site.register(Room, AdminRoom)