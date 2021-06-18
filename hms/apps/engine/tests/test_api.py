# Copyright (C) 2021 Ibrahem Mouhamad

from rest_framework.test import APIClient, APITestCase

from .test_models import create_dummy_db_users

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

    def admin_login_successed(self):
        self.assertTrue(self.client.login(username=self.admin_username, password=self.admin_password))

    def admin_login_failed(self):
        self.assertTrue(self.client.login(username=self.admin_username, password="wrong password"))