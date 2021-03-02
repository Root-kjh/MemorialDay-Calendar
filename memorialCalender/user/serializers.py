from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id']

    def modify_password(self, new_password):
        self.password = new_password
        self.is_valid(raise_exception=True)
        self.
        self.save()
        return {'message' : 'True'}

    def delete(self):
        username = self.get("username")
        password = self.get("password")
        user =  authenticate(username=username, password=password)

        if user is None:
            return {'message': 'Password Not Matched'}

        User.objects.filter(username=username).delete()
        return {'message' : 'True'}