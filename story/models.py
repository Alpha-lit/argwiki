# story/models.py
from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(help_text="Supports basic HTML for emphasis.")
    image = models.ImageField(upload_to="rooms/", blank=True, null=True)

    # Optional SFX to play when entering this room (short clip only, no music)
    sfx_enter = models.FileField(
        upload_to="sfx/rooms/",
        blank=True,
        null=True,
        help_text="Upload a short sound effect (mp3, wav, ogg)"
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

class Tape(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    video_file = models.FileField(upload_to="tapes/", null=True, blank=True)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="characters/", null=True, blank=True)

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="cast/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} as {self.role}"


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news/", null=True, blank=True)

    def __str__(self):
        return self.title