import pytest
import json
import unittest

from app import create_app
app = create_app()

class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.user = {
            "username": "username",
            "email": "email@user.com",
            "password": "yourpassword",
            "confirmPassword": "yourpassword"
        }

    def test_api_can_signup_user(self):
        response = self.client.post('/api/v1/users', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_api_cannot_post_data_without_username_field(self):
        payload = {'email': 'email@user.com', 'password': 'password', 'confirmPassword': 'password'}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["username required"])

    def test_api_cannot_post_data_without_email_field(self):
        payload = {'username': 'username', 'password': 'password', 'confirmPassword': 'password'}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["email required"])

    def test_api_cannot_post_data_without_password_field(self):
        payload = {'username': 'username', 'email': 'email@user.com', 'confirmPassword': 'password'}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["password required"])

    def test_api_cannot_post_data_without_confirmPassword_field(self):
        payload = {'username': 'username', 'email': 'email@user.com', 'password': 'password'}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["confirmPassword required"])

    def test_api_cannot_post_data_without_username_data(self):
        payload = {'username': ' ', 'email': 'email@user.com', 'password': 'password', 'confirmPassword': 'password'}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["username cannot be empty"])

    def test_api_cannot_post_data_without_email_data(self):
        payload = {'username': 'username', 'email': ' ', 'password': 'password', 'confirmPassword': 'password'}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["email cannot be empty"])

    def test_api_cannot_post_data_without_password_data(self):
        payload = {'username': 'username', 'email': 'email@user.com', 'password': ' ', 'confirmPassword': 'password'}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["password cannot be empty"])

    def test_api_cannot_post_data_without_confirmPassword_data(self):
        payload = {'username': 'username', 'email': 'email@user.com', 'password': 'password', 'confirmPassword': ''}
        response = self.client.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["confirmPassword cannot be empty"])
 

if __name__ == '__main__':
    unittest.main()