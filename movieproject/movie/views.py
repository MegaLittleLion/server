from django.shortcuts import render
from .models import Movie, Staff
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView
import requests

# Create your views here.

@api_view(['GET'])
def init_db(request):
    url = "https://api.hufs-likelion-movie.kro.kr/movies"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        movie_obj = Movie.objects.create(
            title_kor=movie['title_kor'],
            title_eng=movie['title_eng'],
            rating_aud=movie['rating_aud'],
            rating_cri=movie['rating_cri'],
            rating_net=movie['rating_net'],
            genre=movie['genre'],
            showtimes=movie['showtimes'],
            release_date=movie['release_date'],
            rate=movie['rate'],
            summary=movie['summary']
        )
    return Response({'message': 'DB init success'})