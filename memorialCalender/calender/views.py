from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CalenderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Calender
from lib.response_form import CREATED_RESPONSE, SUCCESS_RESPONSE, PERMISSION_DENIED_RESPONSE

class CalenderViewSet(viewsets.GenericViewSet):
    queryset = Calender.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CalenderSerializer

    def create(self, request, user_pk=None):
        user = request.user
        if int(user_pk) != user.id:
            print("test")
            return PERMISSION_DENIED_RESPONSE
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        calender = serializer.create(serializer.validated_data, request.user.id)
        calender.save()
        return CREATED_RESPONSE

    def list(self, request, user_pk=None):
        user = request.user
        if int(user_pk) != user.id:
            return PERMISSION_DENIED_RESPONSE

        serializer = self.get_serializer(Calender.objects.filter(user=user.id), many=True) 
        return Response(serializer.data)

    def update(self, request, user_pk=None, pk=None):
        user = request.user
        calender = self.get_object()

        if int(user_pk) != user.id or calender.user_id != request.user.id:
            return PERMISSION_DENIED_RESPONSE

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=calender, validated_data=serializer.validated_data)
        return SUCCESS_RESPONSE

    def destroy(self, request, user_pk=None, pk=None):
        user = request.user
        calender = self.get_object()

        if int(user_pk) != user.id or calender.user_id != request.user.id:
            return PERMISSION_DENIED_RESPONSE
        
        calender.delete()
        return SUCCESS_RESPONSE