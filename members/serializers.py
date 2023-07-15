from .models import CustomUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'nickname']


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=100)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'nickname': self.validated_data.get('nickname', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.nickname = self.cleaned_data.get('nickname')
        user.save()
        adapter.save_user(request, user, self)
        return user

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