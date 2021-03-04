from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from rest_framework.views import APIView
from .serializers import CalenderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .models import Calender
import logging

@permission_classes([IsAuthenticated])
class CalenderView(generics.GenericAPIView):
    serializer_class = CalenderSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        calender = serializer.create(serializer.validated_data, request.user.id)
        calender.save()
        return Response({"message" : "True"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        logger = logging.getLogger(__name__)
        logger.warning("test")
        user = request.user
        serializer = CalenderSerializer(Calender.objects.filter(user=user.id), many=True) 
        return Response(serializer.data)

    def delete(self, requesst, id):
        user = requesst.user
        logger = logging.getLogger(__name__)
        logger.warning("test")
        logger.warning(id)
        if not Calender.objects.filter(id = id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        calender = Calender.objects.filter(id=id).first()
        if calender.user.id != user.id:
            return Response({"Message" : "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)
        calender.delete()
        return Response({"Message" : "True"})

    def put(self, request, id):
        user = request.user
        if not Calender.objects.filter(id = id).exists():
            return Response({"Message" : "Not Exists Calender"}, status=status.HTTP_404_NOT_FOUND)
        calender = Calender.objects.filter(id=id).first()
        if calender.user.id != user.id:
            return Response({"Message" : "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)
        request.data['user'] = user.id
        new_calender_data = CalenderSerializer(data=request.data)
        new_calender_data.is_valid(raise_exception=True)
        CalenderSerializer.update(self, calender, validated_data=new_calender_data.validated_data)
        return Response({"message" : "True"})