from .models import CustomUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'nickname']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'pwcheck', 'nickname']


class UsernameUniqueCheckSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, min_length=1, max_length=30,
                                     validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    class Meta:
        model = CustomUser
        fields = ['username']


# 닉네임 중복 검사
class NicknameUniqueCheckSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(required=True, min_length=1, max_length=30,
                                     validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    class Meta:
        model = CustomUser
        fields = ['nickname']