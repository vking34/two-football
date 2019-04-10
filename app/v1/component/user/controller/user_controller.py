from flask import jsonify, Blueprint, request
from marshmallow import ValidationError
from ..model.user import User
from ..schema.user_schema import UserSchema
from app.v1.generic.response.error_response import USER_NOT_FOUND, ALREADY_USED_USERNAME, ALREADY_USED_EMAIL, ALREADY_USED_PHONE
from app.v1.generic.response.status_code import *
from app.v1.generic.util.authorization_filter import pre_authorize
from app.v1.generic.constant.role_constant import *

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users', methods=['GET'])
def get_users():
    schema = UserSchema(many=True)
    print(schema.dump(User.find_users()).data)
    return jsonify({'students': schema.dump(User.find_users()).data}), OK


@users_blueprint.route('/users/<int:user_id>', methods=['PUT'])
@pre_authorize(ROLE_USER)
def update_user(user_id):
    global result
    request_user = request.json
    schema = UserSchema()
    try:
        result = schema.load(request_user)
    except ValidationError as error:
        print(error)

    if len(result.errors) != 0:
        return jsonify(
            {
                'status': False,
                'errors': result.errors
            }
        )

    user_record = User.find_user_by_id(user_id)
    if user_record is None:
        return jsonify(USER_NOT_FOUND), BAD_REQUEST

    username = request_user.get('username')
    name = request_user.get('name')
    picture = request_user.get('picture')
    email = request_user.get('email')
    phone = request_user.get('phone')

    if user_record.username != username:
        if User.find_user_by_username(username) is not None:
            return jsonify(ALREADY_USED_USERNAME), BAD_REQUEST
    if user_record.email != email:
        if User.find_user_by_email(email) is not None:
            return jsonify(ALREADY_USED_EMAIL), BAD_REQUEST
    if user_record.phone != phone:
        if User.find_user_by_phone(phone) is not None:
            return jsonify(ALREADY_USED_PHONE), BAD_REQUEST

    user_record = User.update_user_by_id(user_id, username, name, picture, phone, email)
    schema = UserSchema()
    data = schema.dump(user_record).data

    return jsonify({
        'status': True,
        'user': data
    }), OK
