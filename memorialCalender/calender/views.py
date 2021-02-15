from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import CalenderSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics

@permission_classes([IsAuthenticated])
class ShowCalender(generics.GenericAPIView):
    serializer_class = CalenderSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message" : "Request Body Error."}, status=status.status.HTTP_409_CONFLICT)
        
        serializer.is_valid(raise_exception=True)
        serializer.save(user = self.request.user)
        return Response({"message" : "True"}, status=status.status.HTTP_201_CREATED)