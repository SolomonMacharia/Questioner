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

    # def test_api_cannot_create_rsvp_without_meetupId(self):
    #     payload = {'topic': 'topic', 'status': 'status'}
    #     response = self.client.post('/meetups/1/rsvps', data=json.dumps(payload), content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #     result = json.loads(response.data)
    #     self.assertEqual(result['errors'], ["meetupId required"])

    # def test_api_cannot_create_rsvp_without_topic(self):
    #     payload = {'meetupId': 834, 'status': 'status'}
    #     response = self.client.post('/meetups/1/rsvps', data=json.dumps(payload), content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #     result = json.loads(response.data)
    #     self.assertEqual(result['errors'], ["topic required"])

    # def test_api_cannot_create_rsvp_without_status(self):
    #     payload = {'meetupId': 834, 'topic': 'topic'}
    #     response = self.client.post('/meetups/1/rsvps', data=json.dumps(payload), content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #     result = json.loads(response.data)
    #     self.assertEqual(result['errors'], ["status required"])