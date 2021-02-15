from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CalenderSerializer, UserSerializer
from calender.models import Calender

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    permission_classes = [permissions.IsAdminUser]