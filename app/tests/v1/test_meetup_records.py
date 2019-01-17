import os
from datetime import datetime
import pytest
import unittest
import json
from app import create_app

from app.api.v1.models.meetup_record_models import MeetupRecord
from ...api.v1.views.meetup_record_views import meetup

class TestQuestionModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.meetup = {
            "meetupId": "meetupId",
            "topic": "topic",
            "location": "The location",
            "images": "images",
            "tags": "tags"
        }
    def tearDown(self):
        del meetup.all_meetup_records[:]

    def test_api_can_create_a_meetup_record(self):
        res = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("The location", str(self.meetup))
        self.assertIn("images", str(self.meetup))

    def test_api_cannot_post_data_without_images(self):
        payload = {'location': 'location', 'tags': 'tags', 'topic': 'topic'}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["images required"])

    def test_api_cannot_post_data_without_location(self):
        payload = {'images': 'images', 'tags': 'tags', 'topic': 'topic'}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["location required"])

    def test_api_cannot_post_data_without_tags(self):
        payload = {'images': 'images', 'location': 'location', 'topic': 'topic'}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["tags required"])

    def test_api_cannot_post_data_without_topic(self):
        payload = {'images': 'images', 'location': 'location', 'tags': 'tags'}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["topic required"])

    def test_api_cannot_post_data_without_image_data(self):
        payload = {'images': '', 'topic': 'topic', 'location': 'location', 'tags': 'tags'}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["images cannot be empty"])

    def test_api_cannot_post_data_without_topic_data(self):
        payload = {'images': 'images', 'topic': '', 'location': 'location', 'tags': 'tags'}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["topic cannot be empty"])

    def test_api_cannot_post_data_without_location_data(self):
        payload = {'images': 'images', 'topic': 'topic', 'location': '', 'tags': 'tags'}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["location cannot be empty"])

    def test_api_cannot_post_data_without_tags_data(self):
        payload = {'images': 'images', 'topic': 'topic', 'location': 'location', 'tags': ''}
        response = self.client.post('/api/v1/meetups', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['errors'], ["tags cannot be empty"])

    

    def test_api_can_fetch_all_meetup_records(self):
        res = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/api/v1/meetups/upcoming', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn("The location", str(self.meetup))

    def test_api_can_fetch_single_meetup_record(self):
        res = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/api/v1/meetups/upcoming/1', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_api_can_delete_record(self):
        res = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client.delete('/api/v1/meetups/upcoming/1/delete', content_type='application/json')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()