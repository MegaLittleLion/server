from django.contrib.auth import authenticate
from django.db import IntegrityError
from requests import Response
from rest_framework.exceptions import APIException, ValidationError

from .models import CustomUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomValidationError(APIException):

    default_detail = 'Validation error'
    default_code = 'invalid'

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'nickname']


class CustomRegisterSerializer(RegisterSerializer):

        password1 = serializers.CharField(error_messages={'blank': '비밀번호를 설정하세요.'})
        password2 = serializers.CharField(error_messages={'blank': '비밀번호를 설정하세요.'})
        nickname = serializers.CharField(max_length=50, validators=[
            UniqueValidator(queryset=CustomUser.objects.all(), message='닉네임이 이미 사용중입니다.')]
                                         , error_messages={'blank': '닉네임을 입력하세요.'})
        username = serializers.CharField(max_length=50, error_messages={'blank': '이름을 입력하세요.'})
        # subscription = serializers.BooleanField(default=False)
        # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED,
        #                                error_messages={'blank': '이메일을 입력하세요.'})

        class Meta:
            model = CustomUser
            fields = ['password', 'nickname', 'username']

        def get_cleaned_data(self):
            super(CustomRegisterSerializer, self).get_cleaned_data()
            return {
                # 'email': self.validated_data.get('email', ''),
                'password1': self.validated_data.get('password1', ''),
                'password2': self.validated_data.get('password2', ''),
                'nickname': self.validated_data.get('nickname', ''),
                'username': self.validated_data.get('name', ''),
                # 'subscription': self.validated_data.get('subscription', ''),
            }

        def save(self, request):
            adapter = get_adapter()
            user = adapter.new_user(request)
            self.cleaned_data = self.get_cleaned_data()
            user.nickname = self.cleaned_data.get('nickname')
            user.username = self.cleaned_data.get('name')
            # user.subscription = self.cleaned_data.get('subscription')
            user.save()
            adapter.save_user(request, user, self)
            return user
    # nickname = serializers.CharField(max_length=100)
    #
    # class Meta:
    #     model = CustomUser
    #     fields = ['id', 'username', 'password', 'nickname']
    #     # validators = [
    #     #     UniqueTogetherValidator(
    #     #         queryset=CustomUser.objects.all(),
    #     #         fields=('username'),
    #     #         message="이미 존재하는 회원"
    #     #     )
    #     # ]
    # def get_cleaned_data(self):
    #     super(CustomRegisterSerializer, self).get_cleaned_data()
    #     return {
    #         'username': self.validated_data.get('username', ''),
    #         'password1': self.validated_data.get('password1', ''),
    #         'password2': self.validated_data.get('password2', ''),
    #         'nickname': self.validated_data.get('nickname', ''),
    #     }
    #
    #
    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     user.username = self.cleaned_data.get('username')
    #     user.nickname = self.cleaned_data.get('nickname')
    #
    #     try:
    #         self.cleaned_data['password1'] == self.cleaned_data['password2']
    #     except:
    #         msg = 'The two password fields not match.'
    #         raise serializers.ValidationError({'detail': msg})
    #
    #     user.set_password(self.cleaned_data['password1'])
    #
    #     try:
    #         user.save()
    #     except:
    #         msg = 'A user with that username already exists.'
    #         raise serializers.ValidationError({'detail': msg})
    #
    #     adapter.save_user(request, user, self)
    #     return user

    # def validate(self, data):
    #     id = data.get('id', None)
    #
    #     if CustomUser.objects.filter(id=id).exists():
    #         raise serializers.ValidationError("uesr already exists")
    #     return data


class CustomLoginSerializer(serializers.Serializer):


    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise CustomValidationError(msg)
                attrs['user'] = user
                return attrs
            else:
                msg = 'invalid id and pw'
                raise CustomValidationError(Response(msg))
        else:
            msg = 'Must include "username" and "password".'
            raise CustomValidationError(msg)

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     password = serializers.CharField(max_length=128)
#
#
# class SignupSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'pwcheck', 'nickname']
#

# class UsernameUniqueCheckSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(required=True, min_length=1, max_length=30,
#                                      validators=[UniqueValidator(queryset=CustomUser.objects.all())])
#
#     class Meta:
#         model = CustomUser
#         fields = ['username']
#

# 닉네임 중복 검사
class NicknameUniqueCheckSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(required=True, min_length=1, max_length=30,
                                     validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    class Meta:
        model = CustomUser
        fields = ['nickname']