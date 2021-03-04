from rest_framework.response import Response
from .serializers import PasswordModifySerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    
    def partial_update(self, request, pk=None):
        user = self.get_object()
        if user.id == request.user.id:
            serializer = PasswordModifySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = self.request.user
            user.set_password(serializer.data.get("password"))
            user.save()
            return Response({"message" : "True"})
        else:
            return Response({"Message" : "Permission Denied"}, status = status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        user = self.get_object()
        if user.id == request.user.id:
            user.delete()
            return Response({"message" : "True"})
        else:
            return Response({"Message" : "Permission Denied"}, status = status.HTTP_403_FORBIDDEN)