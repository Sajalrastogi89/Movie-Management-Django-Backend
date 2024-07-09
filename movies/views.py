from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'release_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.query_params.get('sort_by')
        if sort_by:
            queryset = queryset.order_by(sort_by)
        return queryset

class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

@api_view(['POST'])
def vote_movie(request, pk, vote_type):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=404)
    
    if vote_type == 'upvote':
        movie.votes += 1
    elif vote_type == 'downvote':
        movie.votes -= 1
    else:
        return Response({'error': 'Invalid vote type'}, status=400)

    movie.save()
    return Response({'message': 'Vote recorded', 'votes': movie.votes})
