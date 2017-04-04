# Making list of the games
def making_list_of_games(file_name):
    with open(file_name, "r") as f:
        i = len(f.readlines())
    with open(file_name, "r") as f:
        games = []
        for j in range(i):
            line = list(f.readline().split("\t"))
            line[len(line)-1] = (line[len(line)-1])[:-1]
            games.append(line)
    return games


# Making sorted without using built-in functions
def making_sort_of_list(list_name):
    for k in range(len(list_name)):
        for l in range(len(list_name)-1):
            m = 0
            while m < min([len(list_name[l]), len(list_name[l + 1])]):
                if list_name[l][m].lower() > list_name[l + 1][m].lower():
                    changing = list_name[l + 1]
                    list_name[l + 1] = list_name[l]
                    list_name[l] = changing
                    m = min([len(list_name[l]), len(list_name[l + 1])])
                elif list_name[l][m].lower() < list_name[l + 1][m].lower():
                    m = min([len(list_name[l]), len(list_name[l + 1])])
                else:
                    if m == min([len(list_name[l]), len(list_name[l + 1])])-1:
                        if len(list_name[l]) < len(list_name[l + 1]):
                            m += 1
                        else:
                            changing = list_name[l + 1]
                            list_name[l + 1] = list_name[l]
                            list_name[l] = changing
                            m += 1
                    else:
                        m += 1
    return(list_name)


# First question
def count_games(file_name):
    with open(file_name, "r") as f:
        return len(f.readlines())


# Swcond question
def decide(file_name, year):
    games = making_list_of_games(file_name)
    return False if str(year) not in list(games[k][2] for k in range(len(games))) else True


# Third question
def get_latest(file_name):
    games = making_list_of_games(file_name)
    for k in range(len(games)):
        if (str(max([int(games[l][2]) for l in range(len(games))]))) in games[k][2]:
            return games[k][0]


# Fourth question
def count_by_genre(file_name, genre):
    games = making_list_of_games(file_name)
    return list(games[k][3] for k in range(len(games))).count(genre)


# Fifth question
def get_line_number_by_title(file_name, title):
    games = making_list_of_games(file_name)
    try:
        in_list_check = 0
        for k in range(len(games)):
            if title in games[k][0]:
                in_list_check += 1
                return k + 1
        if in_list_check == 0:
            raise Exception
    except:
        return ValueError


# Sixth question
def sort_abc(file_name):
    games = making_list_of_games(file_name)
    return making_sort_of_list(list(games[k][0] for k in range(len(games))))


# Seventh question
def get_genres(file_name):
    games = making_list_of_games(file_name)
    return making_sort_of_list(list(set(list(games[k][3] for k in range(len(games))))))


# Eight question
def when_was_top_sold_fps(file_name):
    games = making_list_of_games(file_name)
    try:
        topFPS = max([float(games[k][1]) if 'First-person shooter' in games[k][3] else 0 for k in range(len(games))])
        if topFPS == 0:
            raise Exception
        for k in range(len(games)):
            if topFPS == float(games[k][1]):
                return int(games[k][2])
    except:
        return ValueError
