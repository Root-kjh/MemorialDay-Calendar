from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import json

PASSWORD_MODIFY_DATA = {"password": "new password"}

class CalenderTests(APITestCase):

    def setUp(self):
        self.client.post("/auth/signup/",{'username': 'John', 'password': 'complex_password'})
        self.user = User.objects.first()
        response = self.client.post("/auth/signin/", {'username': 'John', 'password': 'complex_password'})
        token = json.loads(response.content)['token']
        self.user_id = json.loads(response.content)['id']
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')

    def tearDown(self):
        User.objects.all().delete()

    def get_other_user_jwt(self):
        self.client.post("/auth/signup/",{'username': 'dead', 'password': 'pool'})
        self.user = User.objects.first()
        response = self.client.post("/auth/signin/", {'username': 'dead', 'password': 'pool'})
        token = json.loads(response.content)['token']
        return f'JWT {token}'

    def test_password_modify(self):
        response = self.client.patch(f"/user/{self.user_id}/",PASSWORD_MODIFY_DATA)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(authenticate(username="John", password=PASSWORD_MODIFY_DATA['password']))

    def test_password_modify_other_user(self):
        other_user_jwt = self.get_other_user_jwt()
        self.client.credentials(HTTP_AUTHORIZATION=other_user_jwt)
        response = self.client.patch(f"/user/{self.user_id}/",PASSWORD_MODIFY_DATA)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(authenticate(username="John", password="complex_password"))

    def test_password_modify_not_exist(self):
        response = self.client.patch("/user/-1/",PASSWORD_MODIFY_DATA)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_password_modify_bad_request(self):
        data = {"pw": "test"}
        response = self.client.patch(f"/user/{self.user_id}/",data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(authenticate(username="John", password="complex_password"))

    
    def test_password_modify_no_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION="no jwt")
        response = self.client.patch(f"/user/{self.user_id}/",PASSWORD_MODIFY_DATA)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(authenticate(username="John", password="complex_password"))

    def test_withdraw(self):
        response = self.client.delete(f"/user/{self.user_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 0)

    def test_withdraw_other_user(self):
        other_user_jwt = self.get_other_user_jwt()
        self.client.credentials(HTTP_AUTHORIZATION=other_user_jwt)
        response = self.client.delete(f"/user/{self.user_id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 2)

    def test_withdraw_not_exist(self):
        response = self.client.delete(f"/user/-1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(User.objects.count(), 1)
    
    def test_withdraw_no_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION="no jwt")
        response = self.client.delete(f"/user/{self.user_id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(User.objects.count(), 1)
    