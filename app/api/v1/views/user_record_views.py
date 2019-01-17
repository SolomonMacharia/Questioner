from flask import Blueprint, request, jsonify, abort
from app.api.v1.models.user_models import User
from ..utils.validators import validate

v1_user_blueprint = Blueprint('user', __name__, url_prefix='/api/v1')
user = User()


@v1_user_blueprint.route('/users', methods=['POST'])
def sign_up_user():
    user_data = request.get_json()
    data = validate(user_data, required_fields=["username", "email", "password", "confirmPassword"])
    if type(data) == list:
        return jsonify({"status": 400, "errors": data}), 400

    username = data['username']
    email = data['email']
    password = data['password']
    confirmPassword = data['confirmPassword']
    
    usr = user.create_user(username, email, password, confirmPassword)
    return jsonify({"status": 200, "data": usr})