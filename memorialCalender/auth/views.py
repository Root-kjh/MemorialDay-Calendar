from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import viewsets

class SignupViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response({"message" : "True"}, status=status.HTTP_201_CREATED)
            
class SigninViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = AuthSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['username'] == "None":
            return Response({"message" : "fail"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(user)