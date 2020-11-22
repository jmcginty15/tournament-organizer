from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from models import db, bcrypt, connect_db, Player, Game, Tournament, PlayerTournament
import lichess.api
import os
import requests

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'yeet')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///chess_tourney')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    """Display homepage"""
    tournaments = Tournament.query.order_by(Tournament.start_date.desc())
    return render_template('home.html', tournaments=tournaments)

@app.route('/tournaments/<int:id>')
def tournament(id):
    """Display main tournament page"""
    tournament = Tournament.query.get_or_404(id)
    return render_template('tournament.html')

