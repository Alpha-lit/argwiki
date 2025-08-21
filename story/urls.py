from django.urls import path
from .views import room_view, pick_choice, start, restart_progress

urlpatterns = [
    path("", start, name="start"),
    path("room/<slug:slug>/", room_view, name="room"),
    path("pick/<int:choice_id>/", pick_choice, name="pick_choice"),
    path("restart/", restart_progress, name="restart_progress"),
    #path("debug/", debug_cookies, name="debug_cookies"),
]