from flask import Blueprint, request, jsonify, abort
from app.api.v1.models.user_models import User

v1_user_blueprint = Blueprint('user', __name__, url_prefix='/api/v1')
user = User()


@v1_user_blueprint.route('/users', methods=['POST'])
def sign_up_user():
    data = request.get_json()
    try:
        username = data['username']
        email = data['email']
        password = data['password']
        repeatPassword = data['repeatPassword']
    except KeyError:
        # abort(500, "Messge: All fields must be present!")
        return jsonify({"status": 400, "Error": "All fields must be present!"}), 400
    if data:
        usr = user.create_user(username, email, password, repeatPassword)
    return jsonify({"status": 201, "data": usr}), 201