import os
from datetime import datetime
import pytest
import unittest
import json
from app import create_app

# from app.api.v1.models.question_record_models import QuestionRecord
from ...api.v1.views.question_record_views import question

class TestQuestionModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.question = {
           "qstnId": "qstnId",
            # "createdOn": datetime.now(),
            # "createdBy": uuid4().int, # generate userId
            "meetupId": 1234, 
            "title": "The question title",
            "body": "The question description",
            "votes": "votes"
        }
    def tearDown(self):
        del question.all_question_records[:]

    def test_api_can_post_a_question_record(self):
        response = self.client.post('/api/v1/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("The question title", str(self.question))
        self.assertIn("The question description", str(self.question))

    def test_api_can_get_all_questions(self):
            res = self.client.get('/api/v1/questions', data=json.dumps(self.question), content_type='application/json')
            self.assertEqual(res.status_code, 200)

    def test_api_can_get_one_question(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/api/v1/questions/1', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_api_cannot_get_question_out_of_index(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/api/v1/questions/13', content_type='application/json')
        self.assertEqual(res.status_code, 405,)
        # self.assertIn("Error: The question Id doesn't exist!", str(res))

    def test_api_can_upvote_a_question(self):
        res = self.client.patch('/api/v1/questions/1/upvote', data=json.dumps(self.question))
        self.assertEqual(res.status_code, 200)
    
    def test_api_can_downvote_question(self):
        response = self.client.patch('/api/v1/questions/1/upvote', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 200)
        response = self.client.patch('/api/v1/questions/1/downvote', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()