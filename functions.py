from classes import Pool, Week

def sort_pools(player_list):
    pool_A = []
    pool_B = []
    pool_C = []
    pool_D = []
    semifinal_1 = []
    semifinal_2 = []
    first_place_match = []
    third_place_match = []

    for player in player_list[:16]:
        if player.seed in [1, 8, 9, 16]:
            pool_A.append(player)
        elif player.seed in [2, 7, 10, 15]:
            pool_B.append(player)
        elif player.seed in [3, 6, 11, 14]:
            pool_C.append(player)
        elif player.seed in [4, 5, 12, 13]:
            pool_D.append(player)
    
    for player in player_list[16:]:
        if player.pool == '1':
            semifinal_1.append(player)
        elif player.pool == '2':
            semifinal_2.append(player)
        elif player.pool == 'F':
            first_place_match.append(player)
        elif player.pool == 'T':
            third_place_match.append(player)
    
    return [Pool('A', pool_A), Pool('B', pool_B), Pool('C', pool_C), Pool('D', pool_D), Pool('1', semifinal_1), Pool('2', semifinal_2), Pool('F', first_place_match), Pool('T', third_place_match)]


def sort_weeks(game_list):
    week_1 = []
    week_2 = []
    week_3 = []
    semifinals = []
    finals = []

    for game in game_list:
        if game.week == 1:
            week_1.append(game)
        elif game.week == 2:
            week_2.append(game)
        elif game.week == 3:
            week_3.append(game)
        elif game.week == 4:
            semifinals.append(game)
        elif game.week == 5:
            finals.append(game)
    
    return [Week(1, week_1), Week(2, week_2), Week(3, week_3), Week(4, semifinals), Week(5, finals)]