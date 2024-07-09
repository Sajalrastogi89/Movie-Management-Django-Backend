from django.urls import path
from .views import MovieListCreateView, ActorListCreateView, vote_movie

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('actors/', ActorListCreateView.as_view(), name='actor-list'),
    path('movies/<int:pk>/<str:vote_type>/', vote_movie, name='vote-movie'),
]
