from datetime import datetime


class CurrentPlay(object):
    def __init__(self):
        self.balls = 0
        self.count = 0
        self.outs = 0
        

class Game(object):
    def __init__(self):
        self.sequentialId = 0
        self.gameId = '' 
        self.link = ''
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = '12:00'
        self.timezone = 'UTC'
        self.status = Status()
        self.home = Team()
        self.away = Team()
        self.series = Series()
        self.venue = Venue()

# ---------------------------------------------------------------------

class GameList(object):
    def __init__(self):
        self.games = [Game()]

# ---------------------------------------------------------------------

class Series(object):
    def __init__(self):
        self.games = 0
        self.currentGame = 0
        self.description = ''

# ---------------------------------------------------------------------

class Status(object):
    def __init__(self):
        self.code = ''
        self.description = ''

# ---------------------------------------------------------------------

class Team(object):
    def __init__(self):
        self.teamId = ''
        self.location = 'home'
        self.name = ''
        self.logo = ''
        self.link = ''
        self.wins = 0
        self.losses = 0
        self.percent = 0
        self.runs = 0
        self.hits = 0 
        self.errors = 0
        self.winner = ''
        self.split = ''
    
# ---------------------------------------------------------------------

class Venue(object):
    def __init__(self):
        self.venueId = ''
        self.name = ''
        self.link = ''

# ---------------------------------------------------------------------

