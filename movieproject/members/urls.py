from django.urls import path, include
from .views import NicknameUniqueCheck

app_name = 'members'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('uniquecheck/nickname/', NicknameUniqueCheck.as_view(), name='nickname-uniquecheck'),
]