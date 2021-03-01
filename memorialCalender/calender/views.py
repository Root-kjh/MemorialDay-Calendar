from django.contrib.auth.models import User
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
        user = request.user
        request.data['user'] = user.id
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message" : "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message" : "True"}, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
class ShowCalender(APIView):
    def get(self, request):
        user = request.user
        if Calender.objects.filter(user=user).count() > 0:
            serializer = CalenderSerializer(Calender.objects.filter(user=user.id), many=True) 
            return Response(serializer.data)
        else:
            return Response({"message" : "Calender Data Not Exist"}, status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsAuthenticated])
class DeleteCalender(APIView):
    def get(self, requesst, id):
        user = requesst.user
        if not Calender.objects.filter(id = id).exists():
            return Response({"Message" : "Not Exists Calender"}, status=status.HTTP_204_NO_CONTENT)
        calender = Calender.objects.filter(id=id).first()
        if calender.user.id != user.id:
            return Response({"Message" : "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)
        calender.delete()
        return Response({"Message" : "True"})

@permission_classes([IsAuthenticated])
class UpdateCalender(APIView):
    def post(self, request, id):
        user = request.user
        if not Calender.objects.filter(id = id).exists():
            return Response({"Message" : "Not Exists Calender"}, status=status.HTTP_204_NO_CONTENT)
        calender = Calender.objects.filter(id=id).first()
        if calender.user.id != user.id:
            return Response({"Message" : "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)
        request.data['user'] = user.id
        new_calender_data = CalenderSerializer(data=request.data)
        if not new_calender_data.is_valid(raise_exception=True):
            return Response({"message" : "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        new_calender_data.is_valid(raise_exception=True)
        CalenderSerializer.update(self, calender, validated_data=new_calender_data.validated_data)
        return Response({"message" : "True"})