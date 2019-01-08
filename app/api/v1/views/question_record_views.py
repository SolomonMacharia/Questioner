from flask import jsonify, Blueprint

v1_questions_blueprint = Blueprint('questions', __name__, url_prefix='/api/v1')

@v1_questions_blueprint.route('/questions', methods=['GET'])
def questions():
    return jsonify(True)