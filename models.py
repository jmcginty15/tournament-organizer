from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)


class Player(db.Model):
    """Player"""

    __tablename__ = 'Players'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    score = db.Column(db.Float, default=0)

    def __repr__(self):
        return f'<Player id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, username: {self.username}>'


class Game(db.Model):
    """Game"""

    __tablename__ = 'Games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    white = db.Column(db.Integer, db.ForeignKey('Players.id'), nullable=False)
    black = db.Column(db.Integer, db.ForeignKey('Players.id'), nullable=False)
    url = db.Column(db.String(), nullable=True)
    schedule = db.Column(db.DateTime(timezone=True))
    tournament = db.Column(db.Integer, db.ForeignKey(
        'Tournaments.id'), nullable=False)
    result = db.Column(db.String())

    def __repr__(self):
        return f'<Game id: {self.id}, white: {self.white}, black: {self.black}, url: {self.url}, schedule: {self.schedule}, tournament: {self.tournament}, result: {self.result}>'


class Tournament(db.Model):
    """Tournament"""

    __tablename__ = 'Tournaments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    start_date = db.Column(db.Date())
    time_control = db.Column(db.String(), nullable=False)
    games = db.relationship('Game')
    players = db.relationship('Player', secondary='Player_Tournaments')

    def __repr__(self):
        return f'<Tournament id: {self.id}, name: {self.name}, start_date: {self.start_date}, time_control: {self.time_control}>'


class PlayerTournament(db.Model):
    """Player-Tournament"""

    __tablename__ = 'Player_Tournaments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey(
        'Players.id'), nullable=False)
    tournament_id = db.Column(
        db.Integer, db.ForeignKey('Tournaments.id'), nullable=False)
    seed = db.Column(db.Integer)
    pool = db.Column(db.String(1))
