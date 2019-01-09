from flask import jsonify, Blueprint, request, json
from ..models.question_record_models import QuestionRecord
from datetime import datetime
from uuid import uuid4

v1_questions_blueprint = Blueprint('questions', __name__, url_prefix='/api/v1')

question = QuestionRecord()

@v1_questions_blueprint.route('/questions', methods=['POST'])
def post_question():
    data = request.get_json()

    qstnId = len(question.all_question_records) + 1
    createdOn = datetime.now()
    createdBy = data["createdBy"]
    meetupId = data["meetupId"]
    title = data["title"]
    body = data["body"]
    votes = data["votes"]

    question.create_question(qstnId, createdOn, createdBy, meetupId, title, body, votes )
    return jsonify({
        "status": 201,
        "data": [{
            "qstnId": qstnId,
            "user": uuid4().int, # generate userId
            "meetup": uuid4().int, # generate meetupId
            "title": "The questions' title",
            "body": "The questions description",
            "votes": question.votes
        }]
    }), 201

@v1_questions_blueprint.route('/questions/<int:qstnId>/upvote', methods=['PATCH'])
def upvote(qstnId):
    votes = len(question.votes) + 1
    return jsonify({
        "status": 200,
        "data": [{
            "meetupId": uuid4().int,
            "title": "title",
            "body": "body",
            "votes":votes
        }]
    })
