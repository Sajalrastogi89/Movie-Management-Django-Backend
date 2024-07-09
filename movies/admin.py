from django.contrib import admin
from .models import Movie, Actor, MovieActor

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_date', 'actor_count', 'votes')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'movie_count')

@admin.register(MovieActor)
class MovieActorAdmin(admin.ModelAdmin):
    list_display = ('movie', 'actor')
