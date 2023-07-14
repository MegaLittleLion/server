from django.urls import path

from .views import login, signup, logout, UsernameUniqueCheck, NicknameUniqueCheck

app_name = 'members'

urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout),
    path('uniquecheck/username/', UsernameUniqueCheck.as_view(), name='uniquecheck_username'),
    path('uniquecheck/nickname/', NicknameUniqueCheck.as_view(), name='uniquecheck_nickname'),
]