from .models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from user.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
import hashlib
from rest_framework.response import Response

HASH_SALT = "KJH_MEMORIAL"

def HASH_PASSWORD(password):
    hashed_password = hashlib.sha512(str(password+HASH_SALT).encode('utf-8')).hexdigest()
    return hashed_password

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            data['user_password'] = HASH_PASSWORD(data['user_password'])
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse("True")
            return JsonResponse(serializer.errors, status=400)
        except:
            return JsonResponse({'Error' : "RequestDataInvalid"})
            

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            data['user_password'] = HASH_PASSWORD(data['user_password'])
            serializer = UserSerializer(data=data)
            user = serializer.validated_data
            if serializer.is_valid():
                user = User.objects.filter(user_id=serializer.validated_data['user_id']).first()
                if user and user.user_password == data['user_password']:
                    token, created = Token.objects.get_or_create(user=user)
                    return JsonResponse({'token' : token.key})
            return JsonResponse(serializer.errors, status=400)
        except:
            return JsonResponse({'Error' : "RequestDataInvalid"})