from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('', init_db),
    path('list/', movie_list),
    path('search/', MovieSearch.as_view(), name='movie_search'),
]