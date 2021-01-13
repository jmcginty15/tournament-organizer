from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from models import db, bcrypt, connect_db, Player, Game, Tournament, PlayerTournament, Admin
from classes import DisplayPlayer, Pool, DisplayGame, Week
from functions import sort_pools, sort_weeks
import lichess.api
import datetime
import os
import requests

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'yeet')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///chess_tourney')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    """Display homepage"""
    tournaments = Tournament.query.order_by(Tournament.start_date.desc())
    today = datetime.date.today()
    flash_class = 'danger'
    admin = session.get('admin')
    if admin:
        flash_class = 'success'
    return render_template('home.html', tournaments=tournaments, today=today, flash_class=flash_class)


@app.route('/tournaments/<int:id>')
def tournament(id):
    """Display main tournament page"""
    tournament = Tournament.query.get_or_404(id)
    player_rels = PlayerTournament.query.all()
    players = [DisplayPlayer(player_rel) for player_rel in player_rels]
    pools = sort_pools(players)
    finals = pools[6:]
    semifinals = pools[4:6]
    pools = pools[:4]

    game_queries = Game.query.filter_by(
        tournament=id).order_by(Game.schedule).all()
    games = []
    for game_query in game_queries:
        white = Player.query.get_or_404(game_query.white)
        black = Player.query.get_or_404(game_query.black)
        games.append(DisplayGame(game_query, white, black))
    weeks = sort_weeks(games)

    current_week = weeks[tournament.current_week - 1]
    current_week_ends = datetime.datetime(2021, 1, 24, 18, 0)

    admin = False
    if session.get('admin'):
        admin = True

    return render_template('tournament.html', tournament=tournament, pools=pools, finals=finals, semifinals=semifinals, weeks=weeks, current_week=current_week, current_week_ends=current_week_ends, admin=admin)


@app.route('/games/<int:id>')
def game(id):
    """Return game by id"""
    game_query = Game.query.get_or_404(id)
    white = Player.query.get_or_404(game_query.white)
    black = Player.query.get_or_404(game_query.black)
    game = DisplayGame(game_query, white, black)

    white = {'first_name': white.first_name,
             'last_name': white.last_name,
             'username': white.username,
             'url': white.url,
             'rating': white.rating}

    black = {'first_name': black.first_name,
             'last_name': black.last_name,
             'username': black.username,
             'url': black.url,
             'rating': black.rating}

    return_obj = {'id': game.id,
                  'white': white,
                  'black': black,
                  'url': game.url,
                  'week': game.week,
                  'schedule': game.schedule,
                  'result': game.result}

    return jsonify(return_obj)


@app.route('/games/<int:id>/schedule', methods=['POST'])
def schedule_game(id):
    game = Game.query.get_or_404(id)
    day = request.form['date']
    hour = request.form['hour']
    minute = request.form['minute']
    am_pm = request.form['am-pm']
    year = 2021
    if day == '01':
        year = 2021
    if am_pm == 'PM':
        hour = f'{int(hour) + 12}'
    schedule = f'{year}-{day}T{hour}:{minute}'
    label = 'scheduled'
    if game.schedule:
        label = 'rescheduled'
    game.schedule = schedule
    db.session.commit()
    tournament = game.tournament
    flash(f'Thank you, your game has been {label}.')
    return redirect(f'/tournaments/{tournament}')


@app.route('/games/<int:id>/report', methods=['POST'])
def report_game(id):
    game = Game.query.get_or_404(id)
    white = Player.query.get_or_404(game.white)
    black = Player.query.get_or_404(game.black)
    white.needs_update = True
    black.needs_update = True
    url = request.form['url']
    game.url = url
    game.needs_update = True
    db.session.commit()
    tournament = game.tournament
    flash(f'Thank you, your game has been reported.')
    return redirect(f'/tournaments/{tournament}')


@app.route('/tournaments/<int:id>/admin')
def admin_page(id):
    if session.get('admin'):
        players = Player.query.filter_by(needs_update=True).all()
        game_queries = Game.query.filter_by(needs_update=True).all()

        games = []
        for game_query in game_queries:
            white = Player.query.get_or_404(game_query.white)
            black = Player.query.get_or_404(game_query.black)
            games.append(DisplayGame(game_query, white, black))

        update_ids = [player.id for player in players]
        player_queries = PlayerTournament.query.filter(
            PlayerTournament.player_id.in_(update_ids)).filter_by(tournament_id=id).filter((PlayerTournament.pool == 'F') | (PlayerTournament.pool == 'T')).all()
        players = [DisplayPlayer(player_query)
                   for player_query in player_queries]

        return render_template('admin.html', players=players, games=games, tournament_id=id)
    else:
        flash('Must be logged in as admin to view that page.')
        return redirect(f'/')


@app.route('/admin/login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    user = Admin.authenticate(username, password)
    if user:
        session['admin'] = user.username
        flash(f'Logged in as admin.')
    else:
        flash(f'Incorrect username or password!')
    return redirect('/')


@app.route('/games/<int:id>/<result>', methods=['POST'])
def update_game(id, result):
    admin = session.get('admin')
    if admin:
        game = Game.query.get_or_404(id)
        if result == 'W':
            game.result = '1-0'
        elif result == 'B':
            game.result = '0-1'
        elif result == 'D':
            game.result = '0.5-0.5'
        elif result == 'DF':
            game.result = '0-0'
        else:
            return jsonify({'status': 'failed'})
        game.needs_update = False
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        flash('Must be logged in as admin to do that.')
        return redirect('/')


@app.route('/players/<int:player_id>/<int:tournament_id>/<int:new_score>', methods=['POST'])
def update_player(player_id, tournament_id, new_score):
    admin = session.get('admin')
    if admin:
        player_rel = PlayerTournament.query.filter_by(
            player_id=player_id).filter_by(tournament_id=tournament_id).filter((PlayerTournament.pool == 'F') | (PlayerTournament.pool == 'T')).first()
        player_rel.score = new_score / 100
        player = Player.query.get_or_404(player_id)
        user = lichess.api.user(player.username)
        player.rating = user['perfs']['classical']['rating']
        player.needs_update = False
        db.session.commit()
        return jsonify({'status': 'success', 'new_rating': player.rating})
    else:
        flash('Must be logged in as admin to do that.')
        return redirect('/')
