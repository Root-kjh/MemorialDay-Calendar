from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         read_only_fields = ['id']

class PasswordModifySerializer(serializers.Serializer):
    password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value