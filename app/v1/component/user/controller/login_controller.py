from flask import jsonify, Blueprint, request
from ..schema.authen_form import AuthenticationForm
from ..model.user import User
from app import bcrypt

login_blueprint = Blueprint('login_blueprint', __name__)


@login_blueprint.route('/login', methods=['POST'])
def login():
    global result
    request_login = request.json
    schema = AuthenticationForm()

    result = schema.load(request_login)

    if len(result.errors) != 0:
        return jsonify({
            'status': False,
            'errors': result.errors
        })
    print(request_login.get('username'))

    user = User.find_user_by_username(request_login.get('username'))

    if user is None:
        return jsonify({
            'status': False,
            'message': 'Username/password is wrong',
            'code': 201
        }), 400

    print(user.password)
    if bcrypt.check_password_hash(user.password, request_login.get('password')) is False:
        return jsonify({
            'status': False,
            'message': 'Username/password is wrong',
            'code': 201
        }), 400

    return "1"

