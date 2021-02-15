from rest_framework.response import Response
from rest_framework import status
from .serializers import SigninSerializer, SignupUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics

@permission_classes([AllowAny])
class Signup(generics.GenericAPIView):
    serializer_class = SignupUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message" : "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response({"message" : "True"}, status=status.HTTP_201_CREATED)
            

@permission_classes([AllowAny])
class Signin(generics.GenericAPIView):
    serializer_class = SigninSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message" : "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['username'] == "None":
            return Response({"message" : "fail"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({"token" : user['token']})

@permission_classes([IsAuthenticated])
class PasswordModify(generics.GenericAPIView):
    pass

@permission_classes([IsAuthenticated])
class Withdraw(generics.GenericAPIView):
    pass