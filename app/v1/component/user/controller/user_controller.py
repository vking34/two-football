from flask import jsonify, Blueprint
from ..model.user import User
from ..schema.user_schema import UserSchema

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users', methods=['GET'])
def get_users():
    schema = UserSchema(many=True)
    print(schema.dump(User.find_users()).data)
    return jsonify({'students': schema.dump(User.find_users()).data})


