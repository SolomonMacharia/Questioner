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
            "id": "qstnId",
            # "createdOn": datetime.now(),
            "createdBy": "userId",
            "meetupId": "MeetupId",
            "title": "The question title",
            "body": "The question description",
            "votes": "votes"
        }
    def tearDown(self):
        del question.all_question_records[:]

    def test_api_can_post_a_question_record(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("The question title", str(self.question))
        self.assertIn("The question description", str(self.question))

if __name__ == '__main__':
    unittest.main()