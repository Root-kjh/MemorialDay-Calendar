from django.contrib.auth.models import User
from rest_framework import serializers
from calender.models import Calender

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender