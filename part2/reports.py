# Making list of the games
def making_list_of_games(file_name):
    with open(file_name, "r") as f:
        i = len(f.readlines())
    with open(file_name, "r") as f:
        games = []
        for j in range(i - 1):
            line = (f.readline().split("\t"))
            line[len(line)-1] = (line[len(line)-1])[:-1]
            games.append(line)
        line = (f.readline().split("\t"))
        games.append(line)
    return games


# First question
def get_most_played(file_name):
    games = making_list_of_games(file_name)
    for k in range(len(games)):
        if max([float(games[l][1]) for l in range(len(games))]) == float(games[k][1]):
            return games[k][0]


# Second question
def sum_sold(file_name):
    games = making_list_of_games(file_name)
    return sum(float(games[k][1]) for k in range(len(games)))


# Third question
def get_selling_avg(file_name):
    games = making_list_of_games(file_name)
    return sum(float(games[k][1]) for k in range(len(games))) / len(games)


# Fourth question
def count_longest_title(file_name):
    games = making_list_of_games(file_name)
    return max([len(games[k][0]) for k in range(len(games))])


# Fifth question
def get_date_avg(file_name):
    games = making_list_of_games(file_name)
    return round(sum(int(games[k][2]) for k in range(len(games))) / len(games))


# Sixth question
def get_game(file_name, title):
    games = making_list_of_games(file_name)
    for k in range(len(games)):
        if title == games[k][0]:
            return [games[k][0], float(games[k][1]), int(games[k][2]), games[k][3], games[k][4]]


# Seventh question
def count_grouped_by_genre(file_name):
    games = making_list_of_games(file_name)
    genreDict = dict()
    for k in range(len(games)):
        if games[k][3] in genreDict:
            genreDict[games[k][3]] += 1
        else:
            genreDict[games[k][3]] = 1
    return genreDict


# Eigth question
def get_date_ordered(file_name):
    games = making_list_of_games(file_name)
    for p in range(len(games)):
        for q in range(len(games)-1):
            if int(games[q][2]) < int(games[q + 1][2]):
                changing = games[q + 1]
                games[q + 1] = games[q]
                games[q] = changing
            elif int(games[q][2]) > int(games[q + 1][2]):
                pass
            else:
                m = 0
                while m < min([len(games[q][0]), len(games[q + 1][0])]):
                    if games[q][0][m].lower() > games[q + 1][0][m].lower():
                        changing = games[q + 1]
                        games[q + 1] = games[q]
                        games[q] = changing
                        m = min([len(games[q][0]), len(games[q + 1][0])])
                    elif games[q][0][m].lower() < games[q + 1][0][m].lower():
                        m = min([len(games[q][0]), len(games[q + 1][0])])
                    else:
                        if m == min([len(games[q][0]), len(games[q + 1][0])])-1:
                            if len(games[q][0]) < len(games[q + 1][0]):
                                m += 1
                            else:
                                changing = games[q + 1]
                                games[q + 1] = games[q]
                                games[q] = changing
                                m += 1
                        else:
                            m += 1
    return list(games[k][0] for k in range(len(games)))
