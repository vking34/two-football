from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.v1.config.database_config import *
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    db_uri = 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}'\
                .format(user=DB_USERNAME, pwd=DB_PASSWORD, host=DB_HOST, port=DB_PORT, db=DB_NAME)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.v1.component.user.controller.user_controller import users_blueprint
    from app.v1.component.user.controller.signup_controller import signup_blueprint
    from app.v1.component.user.controller.login_controller import login_blueprint
    from app.v1.component.transaction.controller.transaction_controller import transaction

    app.register_blueprint(signup_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(users_blueprint, url_prefix='/api/v1')
    app.register_blueprint(transaction, url_prefix='/api/v1')

    return app


