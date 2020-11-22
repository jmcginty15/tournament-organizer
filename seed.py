from models import Player, Game, Tournament, PlayerTournament, db
from sqlalchemy.sql import func
from app import app
from math import radians
import datetime

db.reflect()
db.drop_all()
db.create_all()

jm = Player(first_name='Jason', last_name='McGinty', username='jmcginty15')
zm = Player(first_name='Zach', last_name='McGinty', username='zach_mcginty')
eh = Player(first_name='Edward', last_name='Harbeck', username='harbed_325')
jd = Player(first_name='Joe', last_name='Davis', username='Iarwain_Ben-adar')
ad = Player(first_name='Adam', last_name='Darby', username='Hegemon78')
pd = Player(first_name='Paul', last_name='Davison', username='PDavison')
bh = Player(first_name='Britt', last_name='Hoover', username='Dwang_ho')
jr = Player(first_name='Jeff', last_name='Rooney', username='Macondo_Iceman')
br = Player(first_name='Brian', last_name='Reeves', username='lawbooks10')
bhe = Player(first_name='Brian', last_name='Hellstrom', username='BrianHellstrom')
af = Player(first_name='Alex', last_name='Fader', username='afader')
dba = Player(first_name='Dennis', last_name='Baker', username='godelchess')

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
tourney2 = Tournament(name='YeetButt69', start_date=datetime.date(2021, 11, 29), time_control='1000+1000')

db.session.add(tourney)
db.session.add(tourney2)
db.session.commit()

game = Game(white=1, black=2, tournament=1)

db.session.add(game)
db.session.commit()

players = [jm, zm, eh, jd, ad, pd, bh, jr, br, bhe, af, dba]
for player in players:
    player_tournament = PlayerTournament(player_id=player.id, tournament_id=1)
    db.session.add(player_tournament)
db.session.commit()
