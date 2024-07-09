from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def actor_count(self):
        return self.movieactor_set.count()

class Actor(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    def movie_count(self):
        return self.movieactor_set.count()

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie', 'actor')

    def __str__(self):
        return f"{self.actor.name} in {self.movie.title}"
