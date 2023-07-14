from django.shortcuts import render
from .models import Movie, Staff
from .serializers import MovieSerializer, StaffSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView
import requests
from django.shortcuts import redirect
from django.db.models import Count
from django.db.models import Q, F

# Create your views here.

@api_view(['GET'])
def init_db(request):
    url = "https://api.hufs-likelion-movie.kro.kr/movies"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        movie_data = Movie()
        movie_data.title_kor = movie['title_kor']
        movie_data.title_eng = movie['title_eng']
        movie_data.rating_aud = movie['rating_aud']
        movie_data.rating_cri = movie['rating_cri']
        movie_data.rating_net = movie['rating_net']
        movie_data.genre = movie['genre']
        movie_data.showtimes = movie['showtimes']
        movie_data.release_date = movie['release_date']
        movie_data.rate = movie['rate']
        movie_data.summary = movie['summary']
        movie_data.save()
        

        for staff in movie['staff']:
            staff_data = Staff()
            staff_data.movie_title = movie_data
            staff_data.name = staff['name']
            staff_data.role = staff['role']
            staff_data.image_url = staff['image_url']
            staff_data.save()

    return Response({'message': 'DB is initialized!'})

# @api_view(['GET'])
# def movie_list(request):
    # search_movie = request.GET.get('search_movie')
    # if search_movie:
    #     movies = Movie.objects.filter(Q(title_kor__icontains=search_movie) | Q(title_eng__icontains=search_movie))
    # else:
    #     movies = Movie.objects.all()
    # serializer = MovieSerializer(movies, many=True)
    # return Response(serializer.data)

class MovieSearch(APIView):
    def get(self, request):
        title_kor = request.GET.get('title_kor')
        if not title_kor:
            return Response({'error': 'title_kor parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

        movies = Movie.objects.filter(title_kor__icontains=title_kor)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)