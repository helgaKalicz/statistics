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


# Expected output of the function: a number
def count_games(file_name):
    with open(file_name, "r") as f:
        return len(f.readlines())


# Expected output of the function: boolean value
def decide(file_name, year):
    games = making_list_of_games(file_name)
    for k in range(len(games)):
        if str(year) not in games[k]:
            game_in_year = False
    return False if game_in_year else True


# Expected output of the function: the title of the latest game as a string
# Other expectation: if there is more than one, then return the first from the file
def get_latest(file_name):
    games = making_list_of_games(file_name)
    game_line = 0
    year = 0
    for k in range(len(games)):
        if int(games[k][2]) > year:
            game_line = k
            year = int(games[k][2])
    return games[game_line][0]


# Expected output of the function: a number
def count_by_genre(file_name, genre):
    games = making_list_of_games(file_name)
    genreList = []
    genreList.extend(games[k][3] for k in range(len(games)))
    return genreList.count(genre)


# Expected output of the function: a number (if there is no game found, then raises ValueError exception)
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