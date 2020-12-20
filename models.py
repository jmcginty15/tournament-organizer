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
    url = db.Column(db.String(), nullable=False, unique=True)
    rating = db.Column(db.Integer, nullable=False)
    needs_update = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Player id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, username: {self.username}, rating: {self.rating}>'


class Game(db.Model):
    """Game"""

    __tablename__ = 'Games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    white = db.Column(db.Integer, db.ForeignKey('Players.id'), nullable=False)
    black = db.Column(db.Integer, db.ForeignKey('Players.id'), nullable=False)
    url = db.Column(db.String(), nullable=True)
    week = db.Column(db.Integer)
    schedule = db.Column(db.DateTime(timezone=True))
    tournament = db.Column(db.Integer, db.ForeignKey(
        'Tournaments.id'), nullable=False)
    result = db.Column(db.String())
    needs_update = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Game id: {self.id}, white: {self.white}, black: {self.black}, url: {self.url}, schedule: {self.schedule}, tournament: {self.tournament}, result: {self.result}>'


class Tournament(db.Model):
    """Tournament"""

    __tablename__ = 'Tournaments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    time_control = db.Column(db.String(), nullable=False)
    current_week = db.Column(db.Integer, nullable=False, default=1)
    first = db.Column(db.String())
    second = db.Column(db.String())
    third = db.Column(db.String())
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
    pool = db.Column(db.String(2))
    score = db.Column(db.Float, default=0)
    advances = db.Column(db.Boolean, default=False)
    player = db.relationship('Player')


class Admin(db.Model):
    """Admin"""

    __tablename__ = 'Admins'

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(), nullable=False)

    @classmethod
    def register(cls, username, password):
        pw_hash = bcrypt.generate_password_hash(password)
        pw_hash_utf8 = pw_hash.decode('utf8')
        return cls(username=username, password=pw_hash_utf8)

    @classmethod
    def authenticate(cls, username, password):
        user = Admin.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False
