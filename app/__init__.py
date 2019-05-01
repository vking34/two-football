from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.v1.config.database_config import *
from flask_bcrypt import Bcrypt
import threading
import atexit
# from apscheduler.schedulers.background import BackgroundScheduler
from app.v1.config.thread_config import POOL_TIME, fetch3rdAPI


db = SQLAlchemy()
bcrypt = Bcrypt()

fetchingThread = threading.Thread()


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

    def fetch():
        global fetchingThread

        print(fetchingThread.getName())
        fetchingThread = threading.Timer(POOL_TIME, fetch)
        fetchingThread.start()

        match_list = fetch3rdAPI()

        for match in match_list:
            match_id = int(match.get('match_id'))
            print(match_id)

        with app.app_context():
            from app.v1.component.user.model.user import User




    def interrupt_thread():
        global fetchingThread
        fetchingThread.cancel()

    def init_thread():
        global fetchingThread
        print('init')
        fetchingThread = threading.Timer(POOL_TIME, fetch)
        fetchingThread.start()

    init_thread()
    atexit.register(interrupt_thread)



    # scheduler = BackgroundScheduler()
    # scheduler.add_job(func=fetch, trigger='interval', seconds=3 )
    # scheduler.start()
    #
    # atexit.register(lambda: scheduler.shutdown())

    # scheduler = BackgroundScheduler()
    # scheduler.add_job(func=fetch, trigger='interval', seconds=POOL_TIME)
    # scheduler.start()
    #
    # atexit.register(lambda: scheduler.shutdown())

    return app


