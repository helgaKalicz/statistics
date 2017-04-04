import reports


with open('answers_to_Judy.txt', 'w') as f:
    f.write(str(reports.count_games('game_stat.txt')) + '\n')
    f.write(str(reports.decide('game_stat.txt', 2000)) + '\n')
    f.write(reports.get_latest('game_stat.txt') + '\n')
    f.write(str(reports.count_by_genre('game_stat.txt', 'First-person shooter')) + '\n')
    f.write(str(reports.get_line_number_by_title('game_stat.txt', 'Counter-Strike')) + '\n')
    f.write(str(reports.sort_abc('game_stat.txt')) + '\n')
    f.write(str(reports.get_genres('game_stat.txt')) + '\n')
    f.write(str(reports.when_was_top_sold_fps('game_stat.txt')))
