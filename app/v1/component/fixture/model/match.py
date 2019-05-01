from app import db


class Match(db.Model):

    __tablename__ = 'fixture'

    match_id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer, nullable=False)
    match_date = db.Column(db.String(40), nullable=False)
    match_time = db.Column(db.String(40), nullable=False)
    match_hometeam_name = db.Column(db.String(60), nullable=False)
    match_awayteam_name = db.Column(db.String(60), nullable=False)
    match_hometeam_halftime_score = db.Column(db.Integer)
    match_awayteam_halftime_score = db.Column(db.Integer)
    match_hometeam_score = db.Column(db.Integer)
    match_awayteam_score = db.Column(db.Integer)
    yellow_card = db.Column(db.Integer)

    def __init__(self, match_id, league_id, match_date, match_time, match_hometeam_name, match_awayteam_name,
                 match_hometeam_halftime_score, match_awayteam_halftime_score, match_hometeam_score, match_awayteam_score, yellow_card):
        self.match_id = match_id
        self.league_id = league_id
        self.match_date = match_date
        self.match_time = match_time
        self.match_hometeam_name = match_hometeam_name
        self.match_awayteam_name = match_awayteam_name
        self.match_hometeam_halftime_score = match_hometeam_halftime_score
        self.match_awayteam_halftime_score = match_awayteam_halftime_score
        self.match_hometeam_score = match_hometeam_score
        self.match_awayteam_score = match_awayteam_score
        self.yellow_card = yellow_card

    @classmethod
    def find_match_by_id(cls, match_id):
        return cls.query.filter_by(match_id=match_id).first()

