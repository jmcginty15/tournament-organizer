from classes import Pool, Week

def sort_pools(player_list):
    pool_A = []
    pool_B = []
    pool_C = []
    pool_D = []

    for player in player_list:
        if player.seed in [1, 8, 9, 16]:
            pool_A.append(player)
        elif player.seed in [2, 7, 10, 15]:
            pool_B.append(player)
        elif player.seed in [3, 6, 11, 14]:
            pool_C.append(player)
        elif player.seed in [4, 5, 12, 13]:
            pool_D.append(player)
    
    return [Pool('A', pool_A), Pool('B', pool_B), Pool('C', pool_C), Pool('D', pool_D)]


def sort_weeks(game_list):
    week_1 = []
    week_2 = []
    week_3 = []

    for game in game_list:
        if game.week == 1:
            week_1.append(game)
        elif game.week == 2:
            week_2.append(game)
        elif game.week == 3:
            week_3.append(game)
    
    return [Week(1, week_1), Week(2, week_2), Week(3, week_3)]