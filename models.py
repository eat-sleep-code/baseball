
# ---------------------------------------------------------------------
class Status(object):
    code = ''
    description = ''


# ---------------------------------------------------------------------
class Team(object):
    teamId = ''
    location = 'home'
    name = ''
    link = ''
    wins = 0
    losses = 0
    percent = 0
    runs = 0
    hits = 0 
    errors = 0
    winner = ''
    split = ''
    

# ---------------------------------------------------------------------
class Series(object):
    games = 0
    currentGame = 0
    description = ''


# ---------------------------------------------------------------------
class Venue(object):
    venueId = ''
    name = ''
    link = ''


# ---------------------------------------------------------------------

class Game(object):
    gameId = '' 
    link = ''
    date = ''
    time = ''
    status = Status()
    home = Team()
    away = Team()
    series = Series()
    venue = Venue()

# ---------------------------------------------------------------------

class GameList(object):
    games = [Game()]



