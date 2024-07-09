from rest_framework import serializers
from .models import Movie, Actor

class MovieSerializer(serializers.ModelSerializer):
    actor_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'votes', 'actor_count']

class ActorSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Actor
        fields = ['id', 'name', 'date_of_birth', 'movie_count']
