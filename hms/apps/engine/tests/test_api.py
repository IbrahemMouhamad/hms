# Copyright (C) 2021 Ibrahem Mouhamad

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from .test_models import create_dummy_db_users, create_dummy_db_hospital

class ForceLogin:
    def __init__(self, user, client):
        self.user = user
        self.client = client

    def __enter__(self):
        if self.user:
            self.client.force_login(self.user, backend='django.contrib.auth.backends.ModelBackend')

        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if self.user:
            self.client.logout()

class AuthenticationAPITestCase(APITestCase):
    def setUp(self):
        self.admin_username = "admin"
        self.admin_password = "admin"
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        create_dummy_db_users(cls)

    def test_admin_login_successed(self):
        self.assertTrue(self.client.login(username=self.admin_username, password=self.admin_password))

    def test_admin_login_failed(self):
        self.assertFalse(self.client.login(username=self.admin_username, password="wrong password"))

class HospitalGetAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        create_dummy_db_users(cls)
        cls.hospital = create_dummy_db_hospital(cls, "h1", "add1")

    def _run_api_v1_hospitals_id(self, jid, user):
        with ForceLogin(user, self.client):
            response = self.client.get('/api/v1/hospitals/{}'.format(jid))

        return response

    def _check_request(self, response):
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.hospital.id)
        self.assertEqual(response.data["name"], self.hospital.name)
        self.assertEqual(response.data["address"], self.hospital.address)

    def test_api_v1_hospitals_id_admin(self):
        response = self._run_api_v1_hospitals_id(self.hospital.id, self.admin)
        self._check_request(response)
        response = self._run_api_v1_hospitals_id(self.hospital.id + 10, self.admin)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_v1_hospitals_id_no_auth(self):
        response = self._run_api_v1_hospitals_id(self.hospital.id, None)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self._run_api_v1_hospitals_id(self.hospital.id + 10, None)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class HospitalUpdateAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.hospital = create_dummy_db_hospital(self, "h1", "add1")

    @classmethod
    def setUpTestData(cls):
        create_dummy_db_users(cls)

    def _run_api_v1_hospitals_id(self, jid, user, data):
        with ForceLogin(user, self.client):
            response = self.client.put('/api/v1/hospitals/{}'.format(jid), data=data, format='json')

        return response

    def _check_request(self, response, data):
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.hospital.id)
        self.assertEqual(response.data["name"], data.get('name', self.hospital.name))
        self.assertEqual(response.data["address"], data.get('address', self.hospital.address))

    def test_api_v1_hospitals_id_admin(self):
        data = {"name": "another name", "address": "another address"}
        response = self._run_api_v1_hospitals_id(self.hospital.id, self.admin, data)
        self._check_request(response, data)
        response = self._run_api_v1_hospitals_id(self.hospital.id + 10, self.admin, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_v1_hospitals_id_no_auth(self):
        data = {"name": "another name", "address": "another address"}
        response = self._run_api_v1_hospitals_id(self.hospital.id, None, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self._run_api_v1_hospitals_id(self.hospital.id + 10, None, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class HospitalDeleteAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        create_dummy_db_users(cls)
        cls.hospital = create_dummy_db_hospital(cls, "h1", "add1")

    def _run_api_v1_hospitals_id(self, pid, user):
        with ForceLogin(user, self.client):
            response = self.client.delete('/api/v1/hospitals/{}'.format(pid), format="json")

        return response

    def _check_api_v1_hospitals_id(self, user):
        response = self._run_api_v1_hospitals_id(self.hospital.id, user)
        if user:
                self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        else:
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_v1_hospitals_id_admin(self):
        self._run_api_v1_hospitals_id(self.hospital.id, self.admin)

    def test_api_v1_hospitals_id_no_auth(self):
        self._run_api_v1_hospitals_id(self.hospital.id, None)