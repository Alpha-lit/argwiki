# story/models.py
from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(help_text="Supports basic HTML for emphasis.")
    image = models.ImageField(upload_to="rooms/", blank=True, null=True)

    # Optional SFX to play when entering this room (short clip only, no music)
    sfx_enter = models.CharField(
        max_length=200, blank=True, help_text="Relative path under static/story/sfx, e.g. 'door_creak.mp3'"
    )

    # Tab title override when in this room (optional)
    tab_title = models.CharField(max_length=60, blank=True)

    # Flags automatically set when entering (CSV list like: keyA,keyB)
    set_flags_on_enter = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=200)
    next_room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name="prev_choices")

    # Branch gating: require ALL these flags to be present (CSV)
    require_flags = models.CharField(max_length=250, blank=True)

    # On choosing, set these flags (CSV)
    set_flags = models.CharField(max_length=250, blank=True)

    # Optional: play a specific SFX on click/transition
    sfx_on_choose = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.room} -> {self.next_room} ({self.text[:25]})"