from models import Player, Game, Tournament, PlayerTournament, db
from sqlalchemy.sql import func
from app import app
from math import radians
import datetime
import lichess.api

db.reflect()
db.drop_all()
db.create_all()

username='jmcginty15'
user = lichess.api.user(username)
jm = Player(first_name='Jason', last_name='McGinty', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username = 'zach_mcginty'
user = lichess.api.user(username)
zm = Player(first_name='Zach', last_name='McGinty', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='harbed_325'
user = lichess.api.user(username)
eh = Player(first_name='Edward', last_name='Harbeck', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='Iarwain_Ben-adar'
user = lichess.api.user(username)
jd = Player(first_name='Joe', last_name='Davis', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='Hegemon78'
user = lichess.api.user(username)
ad = Player(first_name='Adam', last_name='Darby', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='PDavison'
user = lichess.api.user(username)
pd = Player(first_name='Paul', last_name='Davison', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='Dwang_ho'
user = lichess.api.user(username)
bh = Player(first_name='Britt', last_name='Hoover', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='Macondo_Iceman'
user = lichess.api.user(username)
jr = Player(first_name='Jeff', last_name='Rooney', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='lawbooks10'
user = lichess.api.user(username)
br = Player(first_name='Brian', last_name='Reeves', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='BrianHellstrom'
user = lichess.api.user(username)
bhe = Player(first_name='Brian', last_name='Hellstrom', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='afader'
user = lichess.api.user(username)
af = Player(first_name='Alex', last_name='Fader', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])
username='godelchess'
user = lichess.api.user(username)
dba = Player(first_name='Dennis', last_name='Baker', username=username, url=f'https://lichess.org/@/{username}', rating=user['perfs']['classical']['rating'])

db.session.add(jm)
db.session.add(zm)
db.session.add(eh)
db.session.add(jd)
db.session.add(ad)
db.session.add(pd)
db.session.add(bh)
db.session.add(jr)
db.session.add(br)
db.session.add(bhe)
db.session.add(af)
db.session.add(dba)

db.session.commit()

tourney = Tournament(name='Inaugural OGB Online Chess Championship', start_date=datetime.date(2020, 11, 29), time_control='30+30')

db.session.add(tourney)
db.session.commit()

game1 = Game(white=12, black=4, tournament=1, week=1, result='1-0')
game2 = Game(white=4, black=12, tournament=1, week=1, result='0-1')
game3 = Game(white=3, black=7, tournament=1, week=1, result='0.5-0.5')
game4 = Game(white=7, black=3, tournament=1, week=1, result='0-0')
game5 = Game(white=2, black=6, tournament=1, week=1, schedule=datetime.datetime(2020, 12, 5, 14, 50))
game6 = Game(white=6, black=2, tournament=1, week=1)
game7 = Game(white=5, black=11, tournament=1, week=1, schedule=datetime.datetime(2020, 12, 5, 14, 50))
game8 = Game(white=11, black=5, tournament=1, week=1)
game9 = Game(white=8, black=9, tournament=1, week=1)
game10 = Game(white=9, black=8, tournament=1, week=1)
game11 = Game(white=1, black=10, tournament=1, week=1)
game12 = Game(white=10, black=1, tournament=1, week=1)
game13 = Game(white=12, black=3, tournament=1, week=2)
game14 = Game(white=3, black=12, tournament=1, week=2, schedule=datetime.datetime(2020, 12, 5, 00, 50))
game15 = Game(white=4, black=7, tournament=1, week=2)
game16 = Game(white=7, black=4, tournament=1, week=2, result='1-0')
game17 = Game(white=2, black=5, tournament=1, week=2)
game18 = Game(white=5, black=2, tournament=1, week=2, result='1-0')
game19 = Game(white=6, black=11, tournament=1, week=2)
game20 = Game(white=11, black=6, tournament=1, week=2)
game21 = Game(white=8, black=1, tournament=1, week=2, result='1-0')
game22 = Game(white=1, black=8, tournament=1, week=2)
game23 = Game(white=9, black=10, tournament=1, week=2)
game24 = Game(white=10, black=9, tournament=1, week=2)
game25 = Game(white=12, black=7, tournament=1, week=3)
game26 = Game(white=7, black=12, tournament=1, week=3, result='1-0')
game27 = Game(white=3, black=4, tournament=1, week=3)
game28 = Game(white=4, black=3, tournament=1, week=3)
game29 = Game(white=2, black=11, tournament=1, week=3, result='0-1')
game30 = Game(white=11, black=2, tournament=1, week=3)
game31 = Game(white=5, black=6, tournament=1, week=3)
game32 = Game(white=6, black=5, tournament=1, week=3)
game33 = Game(white=8, black=10, tournament=1, week=3)
game34 = Game(white=10, black=8, tournament=1, week=3)
game35 = Game(white=1, black=9, tournament=1, week=3)
game36 = Game(white=9, black=1, tournament=1, week=3)

db.session.add(game1)
db.session.add(game2)
db.session.add(game3)
db.session.add(game4)
db.session.add(game5)
db.session.add(game6)
db.session.add(game7)
db.session.add(game8)
db.session.add(game9)
db.session.add(game10)
db.session.add(game11)
db.session.add(game12)
db.session.add(game13)
db.session.add(game14)
db.session.add(game15)
db.session.add(game16)
db.session.add(game17)
db.session.add(game18)
db.session.add(game19)
db.session.add(game20)
db.session.add(game21)
db.session.add(game22)
db.session.add(game23)
db.session.add(game24)
db.session.add(game25)
db.session.add(game26)
db.session.add(game27)
db.session.add(game28)
db.session.add(game29)
db.session.add(game30)
db.session.add(game31)
db.session.add(game32)
db.session.add(game33)
db.session.add(game34)
db.session.add(game35)
db.session.add(game36)
db.session.commit()

players = [dba, zm, jr, jm, ad, eh, jd, pd, br, bhe, af, bh]
seed = 1
for player in players:
    if seed in [1, 6, 7, 12]:
        pool = 'A'
    elif seed in [2, 5, 8, 11]:
        pool = 'B'
    elif seed in [3, 4, 9, 10]:
        pool = 'C'
    player_tournament = PlayerTournament(player_id=player.id, tournament_id=1, seed=seed, pool=pool)
    db.session.add(player_tournament)
    seed += 1
db.session.commit()
