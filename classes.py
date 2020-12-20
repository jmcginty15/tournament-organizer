import lichess.api

class DisplayPlayer():

    def __init__(self, player_rel):
        self.id = player_rel.player_id
        self.first_name = player_rel.player.first_name
        self.last_name = player_rel.player.last_name
        self.username = player_rel.player.username
        self.url = player_rel.player.url
        self.seed = player_rel.seed
        self.pool = player_rel.pool
        self.score = player_rel.score
        self.rating = player_rel.player.rating
        self.advances = player_rel.advances

    def update_rating(self):
        user = lichess.api.user(self.username)
        self.rating = user['perfs']['classical']['rating']


class Pool():

    def __init__(self, pool_letter, player_list):
        if pool_letter in ['A', 'B', 'C', 'D']:
            self.name = f'Pool {pool_letter}'
        elif pool_letter == '1':
            self.name = 'Semifinal 1'
        elif pool_letter == '2':
            self.name = 'Semifinal 2'
        elif pool_letter == 'F':
            self.name = 'First Place Match'
        elif pool_letter == 'T':
            self.name = 'Third Place Match'
        self.players = player_list
        self.standings = self.order_standings()
    
    def order_standings(self):
        players = self.players
        ordered_players = [players[0]]
        for i in range(1, len(players)):
            next_player = players[i]
            if next_player.score <= ordered_players[-1].score:
                ordered_players.append(next_player)
            else:
                for j in range(0, len(ordered_players)):
                    if next_player.score > ordered_players[j].score:
                        ordered_players.insert(j, next_player)
                        break
        return ordered_players


class DisplayGame():

    def __init__(self, game, white, black):
        self.id = game.id
        self.white = white
        self.black = black
        self.url = game.url
        self.week = game.week
        self.schedule = game.schedule
        self.result = game.result


class Week():

    def __init__(self, week_number, game_list):
        if week_number < 4:
            self.name = f'Week {week_number}'
        elif week_number == 4:
            self.name = 'Semifinals'
        elif week_number == 5:
            self.name = 'Finals'
        self.games = game_list