from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Calender
import json

UPDATE_CALENDER_DATA = {
    "title": "new_title",
    "start_day": "2021-02-01",
    "cycle_with": "day",
    "cycle_unit": 10
}

CREATE_CALENDER_DATA = {
    "title": "test_title",
    "start_day": "2021-03-01",
    "cycle_with": "day",
    "cycle_unit": 100
}

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

    def create_test_calender(self):
        self.client.post(f"/user/{self.user_id}/calender/", CREATE_CALENDER_DATA)

    def get_other_user_jwt(self):
        self.client.post("/auth/signup/",{'username': 'dead', 'password': 'pool'})
        self.user = User.objects.first()
        response = self.client.post("/auth/signin/", {'username': 'dead', 'password': 'pool'})
        token = json.loads(response.content)['token']
        return f'JWT {token}'

    def test_create_calender(self):
        response = self.client.post(f"/user/{self.user_id}/calender/",CREATE_CALENDER_DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Calender.objects.count(), 1)

    def test_create_calender_bad_request(self):
        data = {
            "title": "test_title",
            "start_day": "2021-03-01",
            "cycle_with": "day"
        }
        response = self.client.post(f"/user/{self.user_id}/calender/",data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Calender.objects.count(), 0)

    def test_create_calender_no_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION="no jwt")
        response = self.client.post(f"/user/{self.user_id}/calender/",CREATE_CALENDER_DATA)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Calender.objects.count(), 0)

    def test_show_calender(self):
        self.create_test_calender()
        response = self.client.get(f"/user/{self.user_id}/calender/")
        response_data = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Calender.objects.first().id, response_data[0]['id'])

    def test_show_calender_no_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION="no jwt")
        response = self.client.get(f"/user/{self.user_id}/calender/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_calender(self):
        self.create_test_calender()
        response = self.client.put(f"/user/{self.user_id}/calender/{Calender.objects.first().id}/",UPDATE_CALENDER_DATA)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Calender.objects.first().title, UPDATE_CALENDER_DATA['title'])

    def test_update_calender_other_user(self):
        self.create_test_calender()
        other_user_jwt = self.get_other_user_jwt()
        self.client.credentials(HTTP_AUTHORIZATION=other_user_jwt)
        response = self.client.put(f"/user/{self.user_id}/calender/{Calender.objects.first().id}/",UPDATE_CALENDER_DATA)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Calender.objects.first().title, CREATE_CALENDER_DATA['title'])

    def test_update_calender_not_exist(self):
        response = self.client.put(f"/user/{self.user_id}/calender/-1/",UPDATE_CALENDER_DATA)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_calender_bad_request(self):
        self.create_test_calender()
        data = {
            "title": "new_title",
            "start_day": "2021-02-01",
            "cycle_with": "day"
        }
        response = self.client.put(f"/user/{self.user_id}/calender/{Calender.objects.first().id}/",data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Calender.objects.first().title, CREATE_CALENDER_DATA['title'])

    def test_update_calender_no_jwt(self):
        self.create_test_calender()
        self.client.credentials(HTTP_AUTHORIZATION="no jwt")
        response = self.client.put(f"/user/{self.user_id}/calender/{Calender.objects.first().id}/",UPDATE_CALENDER_DATA)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Calender.objects.first().title, CREATE_CALENDER_DATA['title'])

    def test_delete_calender(self):
        self.create_test_calender()
        response = self.client.delete(f"/user/{self.user_id}/calender/{Calender.objects.first().id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Calender.objects.count(), 0)

    def test_delete_calender_other_user(self):
        self.create_test_calender()
        other_user_jwt = self.get_other_user_jwt()
        self.client.credentials(HTTP_AUTHORIZATION=other_user_jwt)
        response = self.client.delete(f"/user/{self.user_id}/calender/{Calender.objects.first().id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Calender.objects.count(), 1)

    def test_delete_calender_not_exist(self):
        response = self.client.delete(f"/user/{self.user_id}/calender/-1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_calender_no_jwt(self):
        self.create_test_calender()
        self.client.credentials(HTTP_AUTHORIZATION="no jwt")
        response = self.client.delete(f"/user/{self.user_id}/calender/{Calender.objects.first().id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Calender.objects.count(), 1)