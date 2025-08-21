from django.contrib import admin
from .models import Room, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    fk_name = 'room'
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("room", "text", "next_room")