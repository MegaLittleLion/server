from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser
from .serializers import NicknameUniqueCheckSerializer, CustomRegisterSerializer, CustomLoginSerializer, \
    CustomValidationError

# Create your views here.
class CustomLoginView(APIView):
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except CustomValidationError as e:
            error_detail = dict(e.detail)
            return Response(error_detail, status=status.HTTP_204_NO_CONTENT)

        # 로그인 성공 시 필요한 로직 수행
        # ...
        return Response({'message': 'Login successful'}, status=200)


class NicknameUniqueCheck(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = NicknameUniqueCheckSerializer
    ## 변경
    authentication_classes = [JWTAuthentication]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response({'detail':'available nickname'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail':'nickname is not unique'}, status=status.HTTP_204_NO_CONTENT)