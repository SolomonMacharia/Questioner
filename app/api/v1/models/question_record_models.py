from datetime import datetime


class QuestionRecord():
    """ Creates the question record model """
    def __init__(self, *args):
        self.all_question_records = []

    def create_question(self, qstnId, createdOn, createdBy, meetupId, title, body, votes):
        """ Adds a new question to the all_question_records list """
        self.qstnId = qstnId
        self.createdOn = datetime.now()
        self.createdBy = createdBy
        self.meetupId = meetupId
        self.title = title
        self.body = body
        self.votes = []
        new_question = {
            "question_id": qstnId,
            "createdOn": createdOn,
            "createdBy": createdBy,
            "meetupId": meetupId,
            "title": title,
            "body": body,
            "votes": []

        }
        self.all_question_records.append(new_question)