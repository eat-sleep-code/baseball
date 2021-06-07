import json
import urllib.request
from datetime import datetime
from config import Config
from models import Game, GameList, CurrentPlay, Bases
from utils import Date

favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl, portraitUrl = Config.read()
		
class Data:

# ---------------------------------------------------------------------

	def getSchedule(filterTeam = ''):
		global apiUrl
		global scheduleUrl
		global logoUrl
		global portraitUrl
		localTimezone = datetime.utcnow().astimezone().tzinfo
		with urllib.request.urlopen(scheduleUrl) as request:
			data = json.loads(request.read().decode())
			#print(data)
			schedule = GameList()
			schedule.games.clear()
			dataSource = data['dates'][0]['games']
			if len(dataSource) > 0:
				i = 0
				for gameData in dataSource:
					gameDate = Date.utcToLocal(gameData['gameDate'])
					i = i + 1
					game = Game()
					game.sequentialId = i
					game.gameId = gameData['gamePk']
					game.link = apiUrl + gameData['link']
					game.date = gameDate.strftime('%Y-%m-%d')
					game.time = gameDate.strftime('%-I:%M %p') 
					game.timezone = localTimezone
					game.status.code = gameData['status']['statusCode']
					game.status.description = gameData['status']['detailedState']
					game.basePattern = 'EEE'
					game.inning = 0
					game.inningHalf = 'top'
					game.home.teamId = gameData['teams']['home']['team']['id']
					game.home.location = 'home'
					game.home.name = gameData['teams']['home']['team']['name']
					game.home.logo = logoUrl.replace('[TEAMID]', str(game.home.teamId))
					game.home.link = apiUrl + gameData['teams']['home']['team']['link']
					game.home.wins = gameData['teams']['home']['leagueRecord']['wins']
					game.home.losses = gameData['teams']['home']['leagueRecord']['losses']
					game.home.percent = gameData['teams']['home']['leagueRecord']['pct']

					try:
						game.home.runs = gameData['teams']['home']['score']
						game.home.hits = 0
						game.home.errors = 0 #TODO: Calculate Errors
					except:
						game.home.runs = 0
						game.home.hits = 0
						game.home.errors = 0 #TODO: Calculate Errors
						pass
					
					if game.status.code == 'F':
						game.home.winner = gameData['teams']['home']['isWinner']
					else: 
						game.home.winner = False

					game.home.split = gameData['teams']['home']['splitSquad']
					game.away.teamId = gameData['teams']['away']['team']['id']
					game.away.location = 'away'
					game.away.name = gameData['teams']['away']['team']['name']
					game.away.logo = logoUrl.replace('[TEAMID]', str(game.away.teamId))
					game.away.link = apiUrl + gameData['teams']['away']['team']['link']
					game.away.wins = gameData['teams']['away']['leagueRecord']['wins']
					game.away.losses = gameData['teams']['away']['leagueRecord']['losses']
					game.away.percent = gameData['teams']['away']['leagueRecord']['pct']

					try:
						game.away.runs = gameData['teams']['away']['score']
						game.away.hits = 0
						game.away.errors = 0 #TODO: Calculate Errors
					except:
						game.away.runs = 0
						game.away.hits = 0
						game.away.errors = 0
						pass

					if game.status.code == 'F':
						game.away.winner = gameData['teams']['away']['isWinner']
					else: 
						game.away.winner = False
					
					game.away.split = gameData['teams']['away']['splitSquad']
					game.venue.venueId = gameData['venue']['id']
					game.venue.name = gameData['venue']['name']
					game.venue.link = apiUrl + gameData['venue']['link']
					game.series.games = gameData['gamesInSeries']
					game.series.currentGame = gameData['seriesGameNumber']
					
					try:
						game.series.description = gameData['description']
					except:
						game.series.description = ''
					#print('\n' + str(game.gameId)) 

					if game.status.code == 'I':
						with urllib.request.urlopen(game.link) as request:
							detailData = json.loads(request.read().decode())
							game.basePattern = Data.getBasePattern(detailData['liveData']['plays']['currentPlay']['runners'])
							game.inning = detailData['liveData']['plays']['currentPlay']['about']['inning']
							game.inningHalf = detailData['liveData']['plays']['currentPlay']['about']['halfInning']
							game.outs = detailData['liveData']['plays']['currentPlay']['count']['outs']
							game.home.hits = detailData['liveData']['boxscore']['teams']['home']['teamStats']['batting']['hits']
							game.away.hits = detailData['liveData']['boxscore']['teams']['home']['teamStats']['batting']['hits']
							
					schedule.games.append(game)

			return schedule

# ---------------------------------------------------------------------
	
	def getCurrentPlay(gameLink = ''):
		global apiUrl
		global scheduleUrl
		global logoUrl
		with urllib.request.urlopen(apiUrl + gameLink) as request:
			data = json.loads(request.read().decode())
			playData = data
			awayScore = playData['liveData']['plays']['currentPlay']['result']['awayScore']
			homeScore = playData['liveData']['plays']['currentPlay']['result']['homeScore']
			currentPlay = CurrentPlay()
			currentPlay.status.code = playData['gameData']['status']['statusCode']
			currentPlay.status.description = playData['gameData']['status']['detailedState']
			currentPlay.inning = playData['liveData']['plays']['currentPlay']['about']['inning']
			currentPlay.inningHalf = playData['liveData']['plays']['currentPlay']['about']['halfInning']
			currentPlay.balls = playData['liveData']['plays']['currentPlay']['count']['balls']
			currentPlay.strikes = playData['liveData']['plays']['currentPlay']['count']['strikes']
			currentPlay.outs = playData['liveData']['plays']['currentPlay']['count']['outs']
			currentPlay.pitcher.playerId = playData['liveData']['plays']['currentPlay']['matchup']['pitcher']['id']
			currentPlay.pitcher.name = playData['liveData']['plays']['currentPlay']['matchup']['pitcher']['fullName']
			currentPlay.pitcher.link = apiUrl + playData['liveData']['plays']['currentPlay']['matchup']['pitcher']['link']
			currentPlay.pitcher.portrait = portraitUrl.replace('[PLAYERID]', str(currentPlay.pitcher.playerId))
			currentPlay.pitcher.pitches = playData['liveData']['plays']['currentPlay']['matchup']['pitchHand']['code']
			currentPlay.batter.playerId = playData['liveData']['plays']['currentPlay']['matchup']['batter']['id']
			currentPlay.batter.name = playData['liveData']['plays']['currentPlay']['matchup']['batter']['fullName']
			currentPlay.batter.link = apiUrl + playData['liveData']['plays']['currentPlay']['matchup']['batter']['link']
			currentPlay.batter.portrait = portraitUrl.replace('[PLAYERID]', str(currentPlay.batter.playerId))
			currentPlay.batter.bats = playData['liveData']['plays']['currentPlay']['matchup']['batSide']['code']
			currentPlay.home.teamId = playData['gameData']['teams']['home']['id']
			currentPlay.home.location = 'home'
			currentPlay.home.name = playData['gameData']['teams']['home']['name']
			currentPlay.home.abbreviation = playData['gameData']['teams']['home']['abbreviation']
			currentPlay.home.logo = logoUrl.replace('[TEAMID]', str(currentPlay.home.teamId))
			currentPlay.home.link = apiUrl + playData['gameData']['teams']['home']['link']
			currentPlay.home.league = playData['gameData']['teams']['home']['league']['name']
			currentPlay.home.league = playData['gameData']['teams']['home']['division']['name']
			currentPlay.home.wins = playData['gameData']['teams']['home']['record']['leagueRecord']['wins']
			currentPlay.home.losses = playData['gameData']['teams']['home']['record']['leagueRecord']['losses']
			currentPlay.home.percent = playData['gameData']['teams']['home']['record']['leagueRecord']['pct']
			currentPlay.home.runs = homeScore
			currentPlay.home.hits =  playData['liveData']['boxscore']['teams']['home']['teamStats']['batting']['hits']
			currentPlay.home.errors = 0 #TODO: Calculate Errors
			if currentPlay.status.code == 'F':
				if homeScore > awayScore:
					currentPlay.home.winner = True
				else: 
					currentPlay.home.winner = False
			else: 
				currentPlay.home.winner = False
			currentPlay.away.name = playData['gameData']['teams']['away']['name']
			currentPlay.away.abbreviation = playData['gameData']['teams']['away']['abbreviation']
			currentPlay.away.logo = logoUrl.replace('[TEAMID]', str(currentPlay.away.teamId))
			currentPlay.away.link = apiUrl + playData['gameData']['teams']['away']['link']
			currentPlay.away.league = playData['gameData']['teams']['away']['league']['name']
			currentPlay.away.league = playData['gameData']['teams']['away']['division']['name']
			currentPlay.away.wins = playData['gameData']['teams']['away']['record']['leagueRecord']['wins']
			currentPlay.away.losses = playData['gameData']['teams']['away']['record']['leagueRecord']['losses']
			currentPlay.away.percent = playData['gameData']['teams']['away']['record']['leagueRecord']['pct']
			currentPlay.away.runs = awayScore
			currentPlay.away.hits =  playData['liveData']['boxscore']['teams']['away']['teamStats']['batting']['hits']
			currentPlay.away.errors = 0 #TODO: Calculate Errors
			if currentPlay.status.code == 'F':
				if awayScore > homeScore:
					currentPlay.away.winner = True
				else: 
					currentPlay.away.winner = False
			else: 
				currentPlay.away.winner = False

			try:
				currentPlay.call = playData['liveData']['plays']['currentPlay']['playEvents'][0]['details']['description']
			except: # Handle MLB's Dynamically Changing Structure
				currentPlay.call = ''
				pass

			try:
				currentPlay.rbis = playData['liveData']['plays']['currentPlay']['result']['rbi']
				currentPlay.playEvent = playData['liveData']['plays']['currentPlay']['result']['event']
				currentPlay.playDescription = playData['liveData']['plays']['currentPlay']['result']['description']
			except: # Handle MLB's Dynamically Changing Structure
				currentPlay.rbis = ''
				currentPlay.playEvent = ''
				currentPlay.playDescription = ''
				pass
			
			try:
				currentPlay.pitchType = playData['liveData']['plays']['currentPlay']['playEvents'][0]['details']['type']['description']
				currentPlay.pitchSpeed = playData['liveData']['plays']['currentPlay']['playEvents'][0]['pitchData']['startSpeed']
			except: # Handle MLB's Dynamically Changing Structure
				currentPlay.pitchType = ''
				currentPlay.pitchSpeed = 0
				pass
			
			currentPlay.bases = Data.getBaseStatus(playData['liveData']['plays']['currentPlay']['runners'])
			return currentPlay

# ---------------------------------------------------------------------

	def getBaseStatus(runners):
		global apiUrl
		global portraitUrl
		bases = Bases()
		for runner in runners:
			origin = runner['movement']['originBase']
			start = runner['movement']['start']
			end = runner['movement']['end']
			out = runner['movement']['outBase']
			isOut = runner['movement']['isOut']
			playerId = runner['details']['runner']['id']
			playerName = runner['details']['runner']['fullName']
			playerLink = apiUrl + runner['details']['runner']['link']
			playerPortrait = portraitUrl.replace('[PLAYERID]', str(playerId)) 
				
			if (end == '1B' and isOut == False):
				#print('1st', origin, start, end, out, isOut, playerId, playerName)
				bases.first = True
				bases.onFirst.playerId = playerId
				bases.onFirst.playerName = playerName
				bases.onFirst.link = playerLink
				bases.onFirst.portrait = playerPortrait
			if (end == '2B' and isOut == False):
				#print('2nd', origin, start, end, out, isOut,  playerId, playerName)
				bases.second = True
				bases.onSecond.playerId = playerId
				bases.onSecond.playerName = playerName
				bases.onSecond.link = playerLink
				bases.onSecond.portrait = playerPortrait
			if (end == '3B' and isOut == False):
				#print('3rd', origin, start, end, out, isOut,  playerId, playerName)
				bases.third = True
				bases.onThird.playerId = playerId
				bases.onThird.playerName = playerName
				bases.onThird.link = playerLink
				bases.onThird.portrait = playerPortrait
			#if (end != 'None' and isOut == False):
				#print('Home', origin, start, end, out, isOut,  playerId, playerName)
			#   bases.home = True
			#   bases.scored.playerId = playerId
			#   bases.scored.playerName = playerName
			#   bases.scored.link = playerLink
			#   bases.scored.portrait = playerPortrait
				
		return bases

# ---------------------------------------------------------------------
		
	def getBasePattern(runners):
		bases = Data.getBaseStatus(runners)
		basePattern = ''
		if bases.first == True:
			basePattern = basePattern + 'F'
		else:
			basePattern = basePattern + 'E'

		if bases.second == True:
			basePattern = basePattern + 'F'
		else:
			basePattern = basePattern + 'E'

		if bases.third == True:
			basePattern = basePattern + 'F'
		else:
			basePattern = basePattern + 'E'

		return basePattern
			
# ---------------------------------------------------------------------

	def getPitchType(pitchTypeAbbreviation):
		pitchTypeAbbreviation
		return {
			'CB' : 'Curveball',
			'CH' : 'Changeup',
			'CU' : 'Curveball',
			'EP' : 'Eephus',
			'FA' : 'Fastball',
			'FC' : 'Fastball (Cutter)',
			'FF' : 'Four-Seam Fastball',
			'FO' : 'Pitch Out',
			'FS' : 'Fastball',
			'FT' : 'Two-Seam Fastball',
			'KC' : 'Knuckle-curve',
			'KN' : 'Knuckleball',
			'PO' : 'Pitch Out',
			'SF' : 'Fastball (Split-Fingered)',
			'SI' : 'Fastball (Sinker)',
			'SL' : 'Slider'
		}[pitchTypeAbbreviation] or ''

# ---------------------------------------------------------------------

	def getTeamAbbreviation(team):
		return {
			'Angels' : 'LAA',
			'Astros' : 'HOU',
			'Athletics' : 'OAK',
			'Blue Jays' : 'TOR',
			'Braves' : 'ATL',
			'Brewers' : 'MIL',
			'Cardinals' : 'SLN',
			'Cubs' : 'CHN',
			'D-backs' : 'ARI',
			'Dodgers' : 'LAD',
			'Giants' : 'SF',
			'Indians' : 'CLE',
			'Mariners' : 'SEA',
			'Marlins' : 'MIA',
			'Mets' : 'NYM',
			'Nationals' : 'WAS',
			'Orioles' : 'BAL',
			'Padres' : 'SD',
			'Phillies' : 'PHL',
			'Pirates' : 'PIT',
			'Rangers' : 'TEX',
			'Rays' : 'TB',
			'Red Sox' : 'BOS',
			'Reds' : 'CIN',
			'Rockies' : 'COL',
			'Royals' : 'KAN',
			'Tigers' : 'DET',
			'Twins' : 'MIN',
			'White Sox' : 'CWS',
			'Yankees' : 'NYY'
		}[team] or team

# ---------------------------------------------------------------------
