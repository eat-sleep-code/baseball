import json
import urllib.request
from models import Game, GameList

class Data:

    def getDaysSchedule(scheduleUrl, filterTeam = ''):
        with urllib.request.urlopen(scheduleUrl) as request:
            data = json.loads(request.read().decode())
            daysSchedule = GameList()
            for gameData in data["dates"][0]["games"]:
                game = Game()
                game.gameId = gameData["gamePk"]
                game.link = gameData["link"]
                game.date = gameData["gameDate"][0:10]
                game.time = gameData["gameDate"][11:15]
                game.status.code = gameData["status"]["statusCode"]
                game.status.description = gameData["status"]["detailedState"]
                game.home.teamId = gameData["teams"]["home"]["team"]["id"]
                game.home.location = 'home'
                game.home.name = gameData["teams"]["home"]["team"]["name"]
                game.home.link = gameData["teams"]["home"]["team"]["link"]
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
                game.away.link = gameData["teams"]["away"]["team"]["link"]
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
                game.series.games = gameData["gamesInSeries"]
                game.series.currentGame = gameData["seriesGameNumber"]
                game.series.description = gameData["description"]
                
                print('\n' + str(game.gameId)) # SHOW CORRECT ID FOR THIS LOOP ITERATION
                
                daysSchedule.games = daysSchedule.games[:] + [game]

                
                # DEBUG CODE -- SHOWS THAT THE PRIOR daysSchedule.games ITEMS APPEAR to GET OVERWRITTEN WITH THE LATEST VALUES IN ADDITION TO A NEW ROW BEING APPENDED
                # CORRECT BEHAVIOR WOULD BE THAT PRIOR VALUES ARE UNTOUCHED AND NEW VALUE WOULD BE APPENDED
                menuItems = daysSchedule.games
                print(menuItems)
                for testItem in menuItems:
                    testId = testItem.gameId
                    title = testItem.home.name + ' VS. ' + testItem.away.name
                    print(title)

            return daysSchedule
                
