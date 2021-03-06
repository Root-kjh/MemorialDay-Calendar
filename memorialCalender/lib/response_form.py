from rest_framework.response import Response
from rest_framework import status
CREATED_RESPONSE  = Response({"Message": "Created"}, status=status.HTTP_201_CREATED)
SUCCESS_RESPONSE = Response({"Message": "Success"})
FAILED_RESPONSE = Response({"Message": "Failed"}, status=status.HTTP_400_BAD_REQUEST)
PERMISSION_DENIED_RESPONSE = Response({"Message": "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)