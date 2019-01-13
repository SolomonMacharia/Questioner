from flask import jsonify, Blueprint, request, json
from datetime import datetime
from uuid import uuid4

class QuestionRecord():
    """ Creates the question record model """
    def __init__(self, *args):
        self.all_question_records = []
        self.votes = 0
    def create_question(self, meetupId, title, body,):
        """ Adds a new question to the all_question_records list """
        votes = self.votes
        new_question = {
            "qstnId": len(self.all_question_records) + 1,
            "createdOn": datetime.now(),
            "createdBy": uuid4().int, # generate userId
            "meetupId": meetupId, # generate meetupId
            "title": title,
            "body": body,
            "votes": votes
        }
        self.all_question_records.append(new_question)
        return new_question
        
    def upvote(self, qstnId):
        for qstn in self.all_question_records:
            if qstn['qstnId'] == qstnId:
                qstn['votes'] = qstn['votes'] + 1
                return qstn
    
    def downvote(self, qstnId):
        for qstn in self.all_question_records:
            if qstn['qstnId'] == qstnId:
                if qstn['votes'] != 0:
                    qstn['votes'] = qstn['votes'] - 1
                return qstn