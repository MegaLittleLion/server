from rest_framework import serializers
from dataclasses import field
from .models import Movie, Staff

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary']