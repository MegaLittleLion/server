from django.db import models
# from members.models import CustomUser

# Create your models here.
class Movie(models.Model):
    title_kor = models.TextField(default='')
    title_eng = models.TextField(default='')
    poster_url = models.URLField(max_length=1024)
    rating_aud = models.TextField(default='')
    rating_cri = models.TextField(default='')
    rating_net = models.TextField(default='')
    genre = models.TextField(default='')
    showtimes = models.TextField(default='')
    release_date = models.TextField(default='')
    rate = models.CharField(max_length=20)
    summary = models.TextField(default='')

    def __str__(self):
        return self.title_kor

class Staff(models.Model):
    movie_title = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE, related_name='staff')
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image_url = models.URLField(max_length=1024)

    def __str__(self):
        return self.name
