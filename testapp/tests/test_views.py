from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from testapp.models import Person
from testapp.serializers import PersonSerializer

from django.urls import reverse

from django.core.management import call_command
from tryunitest.utils import *


class GetPersonViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_get_person_view(self):
        client = APIClient()
        # Replace 'get_person_view' with the actual name or path of your view
        url = reverse('testapp:get_person')
        # Make a GET request to the view
        response = client.get(url)
        # Assert the response status code is 200 OK

        try:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            succes_print(f"Test Get Person View Success")
        except AssertionError as e:
            fail_print(f"Test Get Person View Failed : {str(e)}")


class TestInsertPerson(TestCase):
    def setUp(self):
        data_person = {}
        data_person['first_name'] = "test_name"
        data_person['last_name'] = "test_last_name"
        data_person['email'] = "det@gm.com"
        data_person['date_of_birth'] = "2000-01-01"

        self.data_person = data_person

    def test_get_person_view(self):
        # print(self.data_person)
        client = APIClient()
        # Replace 'get_person_view' with the actual name or path of your view
        url = reverse('testapp:insertperson')
        # # Make a GET request to the view
        try:
            response = client.post(url, self.data_person, format='json')
        except Exception as e:
            fail_print(f"{str(e)}")

        # Assert the response status code is 200 OK
        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            succes_print(f"Test Insert Person data Success")
        except AssertionError as e:
            fail_print(f"Test Insert Person data Fail : {str(e)}")
