import json
import urllib.request
from datetime import datetime
from config import Config
from models import Game, GameList
from utils import Date

favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl = Config.read()
		
class Data:

    def getSchedule(filterTeam = ''):
        global apiUrl
        global scheduleUrl
        global logoUrl
        localTimezone = datetime.utcnow().astimezone().tzinfo
        with urllib.request.urlopen(scheduleUrl) as request:
            data = json.loads(request.read().decode())
            schedule = GameList()
            schedule.games.clear()
            dataSource = data["dates"][0]["games"]
            if len(dataSource) > 0:
                i = 0
                for gameData in dataSource:
                    gameDate = Date.UTCtoLocal(gameData["gameDate"])
                    i = i + 1
                    game = Game()
                    game.sequentialId = i
                    game.gameId = gameData["gamePk"]
                    game.link = apiUrl + gameData["link"]
                    game.date = gameDate.strftime('%Y-%m-%d')
                    game.time = gameDate.strftime('%-I:%M %p') 
                    game.timezone = localTimezone
                    game.status.code = gameData["status"]["statusCode"]
                    game.status.description = gameData["status"]["detailedState"]
                    game.home.teamId = gameData["teams"]["home"]["team"]["id"]
                    game.home.location = 'home'
                    game.home.name = gameData["teams"]["home"]["team"]["name"]
                    game.home.logo = logoUrl.replace('[TEAMID]', str(game.home.teamId))
                    game.home.link = apiUrl + gameData["teams"]["home"]["team"]["link"]
                    game.home.wins = gameData["teams"]["home"]["leagueRecord"]["wins"]
                    game.home.losses = gameData["teams"]["home"]["leagueRecord"]["losses"]
                    game.home.percent = gameData["teams"]["home"]["leagueRecord"]["pct"]
                    game.home.runs = 0
                    game.home.hits = 0
                    game.home.errors = 0
                    if game.status.code == 'F':
                        game.home.winner = gameData["teams"]["home"]["isWinner"]
                    else: 
                        game.home.winner = False
                    game.home.split = gameData["teams"]["home"]["splitSquad"]
                    game.away.teamId = gameData["teams"]["away"]["team"]["id"]
                    game.away.location = 'away'
                    game.away.name = gameData["teams"]["away"]["team"]["name"]
                    game.away.logo = logoUrl.replace('[TEAMID]', str(game.away.teamId))
                    game.away.link = apiUrl + gameData["teams"]["away"]["team"]["link"]
                    game.away.wins = gameData["teams"]["away"]["leagueRecord"]["wins"]
                    game.away.losses = gameData["teams"]["away"]["leagueRecord"]["losses"]
                    game.away.percent = gameData["teams"]["away"]["leagueRecord"]["pct"]
                    game.away.runs = 0
                    game.away.hits = 0
                    game.away.errors = 0
                    if game.status.code == 'F':
                        game.away.winner = gameData["teams"]["away"]["isWinner"]
                    else: 
                        game.away.winner = False
                    game.away.split = gameData["teams"]["away"]["splitSquad"]
                    game.venue.venueId = gameData["venue"]["id"]
                    game.venue.name = gameData["venue"]["name"]
                    game.venue.link = apiUrl + gameData["venue"]["link"]
                    game.series.games = gameData["gamesInSeries"]
                    game.series.currentGame = gameData["seriesGameNumber"]
                    try:
                        game.series.description = gameData["description"]
                    except:
                        game.series.description = ''
                    #print('\n' + str(game.gameId)) 

                    schedule.games.append(game)

            return schedule
                
    def getCurrentPlay(gameId = 0):
