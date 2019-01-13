from flask import jsonify, Blueprint, request, json, abort, make_response
from ..models.question_record_models import QuestionRecord
from datetime import datetime
from uuid import uuid4

v1_questions_blueprint = Blueprint('questions', __name__, url_prefix='/api/v1')

question = QuestionRecord()

@v1_questions_blueprint.route('/questions', methods=['POST'])
def post_question():
    data = request.get_json()
    try:
        meetupId = data["meetupId"]
        title = data["title"]
        body = data["body"]
    except KeyError:
        return jsonify({"status": 400, "Error": "All fields must be preset!"}), 400
    if not request.json or not 'title' in request.json or not 'body' in request.json:
        return jsonify({"status": 400, "Error": "Input should be in json format!"}), 400
    elif title == '' or meetupId == '' or body == '' :
        return jsonify({"status": 400, "Error": "Fields cannot be empty!"}), 400
    elif not isinstance(meetupId, int):
        return jsonify({"status": 400, "Error": "meetupId cannot be string!"}), 400
    else:
        new_question = question.create_question(meetupId, title, body)
    return jsonify({"status": 201, "data": new_question}), 201
    
@v1_questions_blueprint.route('/questions', methods=['GET'])
def get_all_questions():
    return jsonify({"All_questions": question.all_question_records}), 200

@v1_questions_blueprint.route('/questions/<int:qstnId>', methods=['GET'])
def get_one_question(qstnId):
    oneqstn = [qstn for qstn in question.all_question_records if qstn["qstnId"] == qstnId]
    if not isinstance(qstnId, int):
        # abort(405, message="id should be an integer"), 405
        return jsonify({"status": 405, "Error": "question {} doesn't exist!".format(qstnId)}), 405
    elif not oneqstn:
        return jsonify({"status": 404, "Error": "question {} doesn't exist!".format(qstnId)}), 405
    return jsonify({"question": oneqstn[0]}), 200

@v1_questions_blueprint.route('/questions/<int:qstnId>/upvote', methods=['PATCH'])
def upvoteqstn(qstnId):
    upvte = question.upvote(qstnId)
    return jsonify({"status": 200, "data": upvte}), 200

@v1_questions_blueprint.route('/questions/<int:qstnId>/downvote', methods=['PATCH'])
def downqstn(qstnId):
    dwnvte = question.downvote(qstnId)
    return jsonify({"status": 200, "data": dwnvte}), 200
