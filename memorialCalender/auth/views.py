from rest_framework.response import Response
from .serializers import AuthSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from lib.response_form import CREATED_RESPONSE, FAILED_RESPONSE

class SignupViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return CREATED_RESPONSE
            
class SigninViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = AuthSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['username'] == "None":
            return FAILED_RESPONSE
        return Response(user)