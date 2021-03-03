from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PasswordModifySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from rest_framework import generics

@permission_classes([IsAuthenticated])
class UserView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def patch(self, request):
        serializer = PasswordModifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        user.set_password(serializer.data.get("password"))
        user.save()
        return Response({"message" : "True"})

    def delete(self, request):
        self.request.user.delete()
        return Response({"message" : "True"})