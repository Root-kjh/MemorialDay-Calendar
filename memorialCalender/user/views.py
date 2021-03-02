from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from rest_framework import generics

@permission_classes([IsAuthenticated])
class UserView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def patch(self, request):
        user = self.get_serializer(data = User.objects.filter(id=request.user.id).first())
        response = user.modify_password(request.data['password'])
        return Response(response)

    def delete(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.delete()
        response = UserSerializer.delete(self, withdraw_user.validated_data)
        return Response(response)