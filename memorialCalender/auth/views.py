from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import generics

@permission_classes([AllowAny])
class Signup(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response({"message" : "True"}, status=status.HTTP_201_CREATED)
            

@permission_classes([AllowAny])
class Signin(generics.GenericAPIView):
    serializer_class = AuthSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data
        if user['username'] == "None":
            return Response({"message" : "fail"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({"token" : user['token']})