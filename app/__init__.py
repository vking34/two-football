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

        # print(fetchingThread.getName())
        fetchingThread = threading.Timer(POOL_TIME, fetch)
        fetchingThread.start()

        match_list = fetch3rdAPI()

        # with app_context to use SQLalchemy
        with app.app_context():
            from app.v1.component.fixture.model.match import Match

            for match in match_list:
                match_id = int(match.get('match_id'))

                # print('--------------------------------------')
                # print(match_id)

                league_id = int(match.get('league_id'))
                if match.get('match_status') == '':
                    hometeam_halftime_score = 0
                    awayteam_halftime_score = 0
                    hometeam_score = 0
                    awayteam_score = 0
                    yellow_card = 0
                else:
                    hometeam_halftime_score = int(match.get('match_hometeam_halftime_score'))
                    awayteam_halftime_score = int(match.get('match_awayteam_halftime_score'))

                    if match.get('match_hometeam_score') == '':
                        hometeam_score = 0
                    else:
                        hometeam_score = int(match.get('match_hometeam_score'))

                    if match.get('match_awayteam_score') == '':
                        awayteam_score = 0
                    else:
                        awayteam_score = int(match.get('match_awayteam_score'))

                    statistics = match.get('statistics')
                    full_time = False
                    for statistic in statistics:
                        if statistic.get('type') == 'yellow cards':
                            yellow_card = int(statistic.get('home')) + int(statistic.get('away'))
                            full_time = True
                            break
                    if full_time is False:
                        yellow_card = 0

                print('match_hometeam_score: ' + str(hometeam_score))
                print('match_hometeam_halftime_score: ' + str(hometeam_halftime_score))
                print('yellow card: ' + str(yellow_card))

                match_record = Match.find_match_by_id(match_id)
                if match_record is None:
                    # print('insert ' + str(match_id))
                    match_record = Match(match_id=match_id,
                                         league_id=league_id,
                                         match_date=match.get('match_date'),
                                         match_time=match.get('match_time'),
                                         match_hometeam_name=match.get('match_hometeam_name'),
                                         match_awayteam_name=match.get('match_awayteam_name'),
                                         match_hometeam_halftime_score=hometeam_halftime_score,
                                         match_awayteam_halftime_score=awayteam_halftime_score,
                                         match_hometeam_score=hometeam_score,
                                         match_awayteam_score=awayteam_score,
                                         yellow_card=yellow_card,
                                         match_status=match.get('match_status')
                                         )
                    match_record.save()
                    continue

                if match.get('match_status') != '' and match_record.match_status != 'FT':
                    # update match
                    # print('update ' + str(match_id))
                    match_record.update(match_hometeam_halftime_score=hometeam_halftime_score,
                                        match_awayteam_halftime_score=awayteam_halftime_score,
                                        match_hometeam_score=hometeam_score,
                                        match_awayteam_score=awayteam_score,
                                        yellow_card=yellow_card,
                                        match_status=match.get('match_status'))
                    continue

                if match.get('match_status') == 'FT' and match_record.match_status != 'FT':
                    print('calculate ' + str(match_id))
                    # calculate bets ...









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


