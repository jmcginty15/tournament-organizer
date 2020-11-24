from classes import Pool, Week

def sort_pools(player_list):
    pool_A = []
    pool_B = []
    pool_C = []

    for player in player_list:
        if player.seed in [1, 6, 7, 12]:
            pool_A.append(player)
        elif player.seed in [2, 5, 8, 11]:
            pool_B.append(player)
        elif player.seed in [3, 4, 9, 10]:
            pool_C.append(player)
    
    return [Pool('A', pool_A), Pool('B', pool_B), Pool('C', pool_C)]


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