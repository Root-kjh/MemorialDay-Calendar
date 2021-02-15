from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from rest_framework.views import APIView
from .serializers import CalenderSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .models import Calender

@permission_classes([IsAuthenticated])
class SetCalender(generics.GenericAPIView):
    serializer_class = CalenderSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message" : "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        
        serializer.is_valid(raise_exception=True)
        serializer.save(user = self.request.user)
        return Response({"message" : "True"}, status=status.status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
class ShowCalender(APIView):
    serializer_class = CalenderSerializer
    def get(self, request, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({"Not Logined"}, status=status.status.HTTP_401_UNAUTHORIZED)
        if Calender.objects.filter(user=user).count() > 0:
            serializer = CalenderSerializer(Calender.objects.filter(user=user))
            return Response(serializer.data)
        else:
            return Response({"message" : "Calender Data Not Exist"}, status=status.HTTP_204_NO_CONTENT)