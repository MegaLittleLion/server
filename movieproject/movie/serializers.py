from rest_framework import serializers
from dataclasses import field
from .models import Movie, Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ['movie_title']

class MovieSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['title_kor', 'title_eng', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary', 'staff']