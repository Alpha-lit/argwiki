from django.urls import path
from .views import *

urlpatterns = [
    path("", start, name="start"),
    path("room/<slug:slug>/", room_view, name="room"),
    path("pick/<int:choice_id>/", pick_choice, name="pick_choice"),
    path("restart/", restart_progress, name="restart_progress"),
    # Tapes
    path("tapes/", tape_list, name="tape_list"),
    path("tapes/<int:pk>/", tape_detail, name="tape_detail"),

    # Characters
    path("characters/", character_list, name="character_list"),
    path("characters/<int:pk>/", character_detail, name="character_detail"),

    # Cast
    path("cast/", cast_list, name="cast_list"),
    path("cast/<int:pk>/", cast_detail, name="cast_detail"),

    # News
    path("news/", news_list, name="news_list"),
    path("news/<int:pk>/", news_detail, name="news_detail"),
]