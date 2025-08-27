# story/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Room, Choice,Tape, Character, Cast, News

# ---------- helpers ----------
def _csv_to_set(csv_str):
    return set([s.strip() for s in csv_str.split(",") if s.strip()]) if csv_str else set()

def _csv_to_list(csv_str):
    return [s.strip() for s in csv_str.split(",") if s.strip()] if csv_str else []

def _list_to_csv(lst):
    return ",".join(lst)


# ---------- start ----------
def start(request):
    first = Room.objects.first()
    if not first:
        return render(request, "story/empty.html")

    progress_slug = request.COOKIES.get("progress")
    if progress_slug and Room.objects.filter(slug=progress_slug).exists():
        last_room = Room.objects.get(slug=progress_slug)
        return render(request, "story/start_choice.html", {
            "last_room": last_room,
            "first_room": first
        })

    return redirect("room", slug=first.slug)


# ---------- room_view ----------
def room_view(request, slug):
    try:
        room = Room.objects.get(slug=slug)
    except Room.DoesNotExist:
        first = Room.objects.first()
        if not first:
            return render(request, "story/empty.html")
        resp = redirect("room", slug=first.slug)
        resp.delete_cookie("progress", path="/")
        resp.delete_cookie("flags", path="/")
        resp.delete_cookie("history", path="/")
        return resp

    flags = _csv_to_set(request.COOKIES.get("flags", ""))
    new_flags = flags | _csv_to_set(room.set_flags_on_enter)

    visible_choices = [
        c for c in room.choices.all()
        if _csv_to_set(c.require_flags).issubset(new_flags)
    ]

    # --- history handling ---
    history = _csv_to_list(request.COOKIES.get("history", ""))

    # If current room is the last recorded, pop it (so back works correctly)
    if history and history[-1] == slug:
        history.pop()

    back_slug = history[-1] if history else None

    resp = render(
        request,
        "story/room.html",
        {
            "room": room,
            "choices": visible_choices,
            "flags": ",".join(sorted(new_flags)),
            "back_slug": back_slug,
        },
    )
    resp.set_cookie("progress", room.slug,
                    max_age=60*60*24*90, samesite="Lax", path="/")
    resp.set_cookie("flags", ",".join(sorted(new_flags)),
                    max_age=60*60*24*90, samesite="Lax", path="/")
    resp.set_cookie("history", _list_to_csv(history),
                    max_age=60*60*24*90, samesite="Lax", path="/")

    return resp


# ---------- pick_choice ----------
def pick_choice(request, choice_id):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")
    choice = get_object_or_404(Choice, id=choice_id)

    flags = _csv_to_set(request.COOKIES.get("flags", ""))
    new_flags = flags | _csv_to_set(choice.set_flags)

    # Build history of rooms we have *visited*
    history = _csv_to_list(request.COOKIES.get("history", ""))
    history.append(choice.room.slug)   # record the room we are leaving

    next_room = choice.next_room
    resp = redirect("room", slug=next_room.slug) if next_room else redirect("start")

    resp.set_cookie("flags", ",".join(sorted(new_flags)),
                    max_age=60*60*24*90, samesite="Lax", path="/")
    resp.set_cookie("history", _list_to_csv(history),
                    max_age=60*60*24*90, samesite="Lax", path="/")

    if choice.sfx_on_choose:
        resp.set_cookie("_cue_sfx", choice.sfx_on_choose,
                        max_age=5, samesite="Lax", path="/")
    return resp


# ---------- restart_progress ----------
def restart_progress(request):
    first = Room.objects.first()
    if not first:
        return render(request, "story/empty.html")
    resp = redirect("room", slug=first.slug)
    resp.delete_cookie("progress", path="/")
    resp.delete_cookie("flags", path="/")
    resp.delete_cookie("history", path="/")
    return resp
def tape_list(request):
    tapes = Tape.objects.all()
    return render(request, "story/tapes/list.html", {"tapes": tapes})

def tape_detail(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    return render(request, "story/tapes/detail.html", {"tape": tape})


# ---- Characters ----
def character_list(request):
    characters = Character.objects.all()
    return render(request, "story/characters/list.html", {"characters": characters})

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, "story/characters/detail.html", {"character": character})


# ---- Cast ----
def cast_list(request):
    cast_members = Cast.objects.all()
    return render(request, "story/cast/list.html", {"cast_members": cast_members})

def cast_detail(request, pk):
    cast_member = get_object_or_404(Cast, pk=pk)
    other_cast = Cast.objects.exclude(pk=pk)  # prepare this in Python, not template
    return render(
        request,
        "story/cast/detail.html",
        {"cast_member": cast_member, "other_cast": other_cast},
    )
# ---- News ----
def news_list(request):
    news_items = News.objects.all().order_by("-published_at")
    return render(request, "story/news/list.html", {"news_items": news_items})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, "story/news/detail.html", {"news_item": news_item})