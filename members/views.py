import generics as generics
from django.shortcuts import render

from django.contrib import auth
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import CustomUser
from .serializers import LoginSerializer, SignupSerializer, UsernameUniqueCheckSerializer, \
    NicknameUniqueCheckSerializer


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data["username"]
        password = request.data["password"]
        try:
            user = CustomUser.objects.get(username=username)
            if not user.check_password(password):
                return Response({"response": "incorrect Password"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response": "No User exist"}, status=status.HTTP_404_NOT_FOUND)

        user = auth.authenticate(
            request=request,
            username=serializer.data['username'],
            password=serializer.data['password']
        )
        if user is not None:
            auth.login(request, user)
            return Response(status=status.HTTP_200_OK)
    return Response({"response": "not valid login"}, status=status.HTTP_400_BAD_REQUEST)


class UsernameUniqueCheck(CreateAPIView):
    serializer_class = UsernameUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(data={'detail':['id available']}, status=status.HTTP_200_OK)
        else:
            detail = dict()
            detail['detail'] = serializer.errors['username']
            return Response(data=detail, status=status.HTTP_400_BAD_REQUEST)


class NicknameUniqueCheck(CreateAPIView):
    serializer_class = NicknameUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(data={'detail':['available nickname']}, status=status.HTTP_200_OK)
        else:
            detail = dict()
            detail['detail'] = serializer.errors['nickname']
            return Response(data=detail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signup(request):

    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        if request.data['pwcheck'] == request.data['password']:
            new_user = serializer.save(password=make_password(serializer.validated_data['password']))
            request.data.pop('pwcheck')
            auth.login(request, new_user)
            return Response(status=status.HTTP_200_OK, data={"detail": "signup successful"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail":"password not same"})
    return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail":"not valid signup"})


@api_view(['POST'])
def logout(request):

    auth.logout(request)
    return Response(status=status.HTTP_200_OK)