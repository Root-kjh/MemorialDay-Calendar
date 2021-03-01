from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SigninSerializer, UserSerializer, WithdrawSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from django.contrib.auth.models import User

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
    serializer_class = SigninSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data
        if user['username'] == "None":
            return Response({"message" : "fail"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({"token" : user['token']})

@permission_classes([IsAuthenticated])
class PasswordModify(APIView):
    def put(self, request):
        user = User.objects.filter(id=request.user.id).first()
        if len(request.data['password'])>128:
            return Response({"message" : "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        response = UserSerializer.modify_password(self, user, request.data['password'])
        return Response(response)

@permission_classes([IsAuthenticated])
class Withdraw(APIView):
    def delete(self, request):
        withdraw_user = WithdrawSerializer(data={'username' : request.user.username, 'password' : request.data['password']})
        withdraw_user.is_valid(raise_exception=True)
        response = WithdrawSerializer.delete(self, withdraw_user.validated_data)
        return Response(response)