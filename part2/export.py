import reports

with open('answers_to_Judy_part_2.txt', 'w') as f:
    f.write(reports.get_most_played('game_stat.txt') + '\n')
    f.write(str(reports.sum_sold('game_stat.txt')) + '\n')
    f.write("%.2f" % (reports.get_selling_avg('game_stat.txt')) + '\n')
    f.write(str(reports.count_longest_title('game_stat.txt')) + '\n')
    f.write(str(reports.get_date_avg('game_stat.txt')) + '\n')
    f.write(str(reports.get_game('game_stat.txt', 'Counter-Strike')) + '\n')
    f.write(str(reports.count_grouped_by_genre('game_stat.txt')) + '\n')
    f.write(str(reports.get_date_ordered('game_stat.txt')))
