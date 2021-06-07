from datetime import datetime

class Bases(object):
    def __init__(self):
        self.first = False
        self.onFirst = Player()
        self.second = False
        self.onSecond = Player()
        self.third = False
        self.onThird = Player()
        self.home = False
        self.scored = Player()

# ---------------------------------------------------------------------

class CurrentPlay(object):
    def __init__(self):
        self.status = Status()
        self.inning = 1
        self.inningHalf = 'top'
        self.balls = 0
        self.strikes = 0
        self.outs = 0
        self.rbis = 0
        self.bases = Bases()
        self.pitcher = Player()
        self.batter = Player()
        self.home = Team()
        self.away = Team()
        self.call = ''
        self.pitchType = ''
        self.pitchSpeed = 0
        
# ---------------------------------------------------------------------

class Game(object):
    def __init__(self):
        self.sequentialId = 0
        self.gameId = 0 
        self.link = ''
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = '12:00'
        self.timezone = 'UTC'
        self.status = Status()
        self.basePattern = ''
        self.inning = 0
        self.inningHalf = 'top'
        self.outs = 0
        self.home = Team()
        self.away = Team()
        self.series = Series()
        self.venue = Venue()

# ---------------------------------------------------------------------

class GameList(object):
    def __init__(self):
        self.games = [Game()]

# ---------------------------------------------------------------------

class Player(object):
    def __init__(self):
        self.playerId = 0
        self.name = ''
        self.link = ''
        self.portrait = ''
        self.bats = ''
        self.pitches = ''

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
        self.teamId = 0
        self.location = 'home'
        self.name = ''
        self.abbreviation = ''
        self.logo = ''
        self.link = ''
        self.league = ''
        self.division = ''
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
        self.venueId = 0
        self.name = ''
        self.link = ''

# ---------------------------------------------------------------------

