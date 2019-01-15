import unittest
import pytest
import json
from app import create_app

app =create_app()

class TestRsvps(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

        self.payload = {
            "meetupId": 1,
            "topic": "The topic",
            "status": "status"
        }

    def test_api_can_create_rsvp(self):
        response = self.client.post('/api/v1/meetups/1/rsvps', data=json.dumps(self.payload), content_type='application/json' )
        self.assertEqual(response.status_code, 201)