from django.contrib import admin
from .models import Room, Choice, Tape, Character, Cast, News

# --- Room / Choice ---
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

# --- Tape ---
@admin.register(Tape)
class TapeAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "video_file")
    search_fields = ("title",)

# --- Character ---
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    search_fields = ("name",)

# --- Cast ---
@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "image")
    search_fields = ("name", "role")

# --- News ---
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "image")
    list_filter = ("published_at",)
    search_fields = ("title", "content")
