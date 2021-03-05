from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
import json

JWT_DECODE_HANDLER = api_settings.JWT_DECODE_HANDLER

class AuthTests(APITestCase):
    
    def tearDown(self):
        User.objects.all().delete()

    def test_signup(self):
        response = self.client.post("/auth/signup/",{'username': 'John', 'password': 'complex_password'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_signup_exist_user(self):
        response = self.client.post("/auth/signup/", {'username': 'John', 'password': 'complex_password'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post("/auth/signup/", {'username': 'John', 'password': 'complex_password'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_signup_bad_request(self):
        response = self.client.post("/auth/signup/",{'username': 'John'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin(self):
        self.client.post("/auth/signup/",{'username': 'John', 'password': 'complex_password'})
        response = self.client.post("/auth/signin/", {'username': 'John', 'password': 'complex_password'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JWT_DECODE_HANDLER(json.loads(response.content)['token'])['username'], "John")

    def test_signin_login_failed(self):
        self.client.post("/auth/signup/",{'username': 'John', 'password': 'complex_password'})
        response = self.client.post("/auth/signin/", {'username': 'John', 'password': 'no password'})
        self.assertEqual(json.loads(response.content)['Message'], "Failed")