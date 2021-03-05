from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Calender
import json

class CalenderTests(APITestCase):

    def setUp(self):
        self.client.post("/auth/signup/",{'username': 'John', 'password': 'complex_password'})
        self.user = User.objects.first()
        response = self.client.post("/auth/signin/", {'username': 'John', 'password': 'complex_password'})
        token = json.loads(response.content)['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')

    def tearDown(self):
        User.objects.all().delete()

    def test_create_calender(self):
        data = {
            "title": "test_title",
            "start_day": "2021-03-01",
            "cycle_with": "day",
            "cycle_unit": 100
        }
        response = self.client.post("/calender/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Calender.objects.count(), 1)

    def test_create_calender_bad_request(self):
        pass

    def test_create_calender_no_jwt(self):
        pass

    def test_show_calender_no_jwt(self):
        pass

    def test_update_calender_other_user(self):
        pass

    def test_update_calender_not_exist(self):
        pass

    def test_update_calender_bad_request(self):
        pass

    def test_update_calender_no_jwt(self):
        pass

    def test_delete_calender_other_user(self):
        pass

    def test_delete_calender_not_exist(self):
        pass

    def test_delete_calender_no_jwt(self):
        pass