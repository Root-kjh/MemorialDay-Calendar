from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import CalenderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Calender

class CalenderViewSet(viewsets.GenericViewSet):
    queryset = Calender.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CalenderSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        calender = serializer.create(serializer.validated_data, request.user.id)
        calender.save()
        return Response({"message" : "True"}, status=status.HTTP_201_CREATED)

    def list(self, request):
        user = request.user
        serializer = CalenderSerializer(Calender.objects.filter(user=user.id), many=True) 
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = request.user
        calender = self.get_object()
        if calender.user_id == request.user.id:
            new_calender_data = CalenderSerializer(data=request.data)
            new_calender_data.is_valid(raise_exception=True)
            CalenderSerializer.update(self, calender, validated_data=new_calender_data.validated_data)
            return Response({"message" : "True"})
        else:
            return Response({"Message" : "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        calender = self.get_object()
        if calender.user_id == request.user.id:
            calender.delete()
            return Response({"Message" : "True"})
        else:
            return Response({"Message" : "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)