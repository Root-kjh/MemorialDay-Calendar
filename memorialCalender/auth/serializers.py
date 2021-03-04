from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model

# JWT 사용을 위한 설정 
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER 
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER 

# 기본 유저 모델 불러오기
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password", None)
        user =  authenticate(username=username, password=password)

        if user is None:
            return {'username': 'None'}
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
            'User with given username and password does not exist'
        )
        return {
            'id' : user.id,
            'username' : user.username,
            'token' : jwt_token
        }