def getCount(howMany, max):
	count = ''
	if int(howMany) == 4 and max == 4:
		count = u"\u25CF \u25CF \u25CF \u25CF"
	elif int(howMany) == 3 and max == 4:
		count = u"\u25CF \u25CF \u25CF \u25CB"
	elif int(howMany) == 2 and max == 4:
		count = u"\u25CF \u25CF \u25CB \u25CB"
	elif int(howMany) == 1 and max == 4:
		count = u"\u25CF \u25CB \u25CB \u25CB"
	elif int(howMany) == 0 and max == 4:
		count = u"\u25CB \u25CB \u25CB \u25CB"
	elif int(howMany) == 3:
		count = u"\u25CF \u25CF \u25CF"
	elif int(howMany) == 2:
		count = u"\u25CF \u25CF \u25CB"
	elif int(howMany) == '1':
		count = u"\u25CF \u25CB \u25CB"
	else:
		count = u"\u25CB \u25CB \u25CB"
	return count

# ---------------------------------------------------------------------

def getPitchType(pitch):
	pitchTypeAbbreviation = pitch.pitchType
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

def getAtBatTeam(game, atBat):
	if getTeamAbbreviation(game.team) == atBat.batter.team:
		output = '[' + game.team + '] vs. ' + game.opponent
	elif getTeamAbbreviation(game.opponent) == atBat.batter.team:
		output = game.team + ' vs. [' + game.opponent + ']'
	else:
		output = game.team + ' vs. ' + game.opponent
	return output

def getPlayer(players, playerID):
	playerRoot = players.xpath("/game/team/player[@id='" + playerID + "']")[0]
	player = Player()
	player.id = playerID
	player.first = playerRoot.get('first')
	player.last = playerRoot.get('last')
	player.team = playerRoot.get('team_abbrev')
	player.number = playerRoot.get('num')
	player.handed = playerRoot.get('rl')
	player.bats = playerRoot.get('bats')
	player.position = playerRoot.get('position')
	player.status = playerRoot.get('status')
	average = playerRoot.get('avg')
	if average.isdigit() == False:
		average = 0
	player.avg = '{0:.3f}'.format(float(average))
	player.hr = playerRoot.get('hr')
	player.rbi = playerRoot.get('rbi')
	if player.position == 'P':
		player.wins = playerRoot.get('wins')
		player.losses = playerRoot.get('losses')
		player.era = float(playerRoot.get('era'))
	return player

# ---------------------------------------------------------------------

def getLatestEvent(game, eventsUrl, players, scoreboardUrl, interval=60):
	try:
		inning = Inning()
		atBat = AtBat()
		pitch = Pitch()

		scoreboardRequest = requests.get(scoreboardUrl)
		scoreboardDocumentBytes = bytes(bytearray(scoreboardRequest.text, encoding='utf-8'))
		scoreboardDocumentXML = etree.XML(scoreboardDocumentBytes)
		gameRoot = scoreboardDocumentXML.xpath("/scoreboard/*/game[@id='" + game.id + "']")[0]
		
		gameStatus = gameRoot.get('status')
		if gameStatus == 'FINAL' or gameStatus == 'GAME_OVER':
			game.status = 'FINAL'
		elif gameStatus == 'PRE_GAME':
			game.status == 'PREGAME'
			
		outs = gameRoot.getparent().get("outs") or 0  # MLB stores items in multiple places?
		parentIter = gameRoot.getparent().iter()
		for child in parentIter:
			if child.tag == 'team' and child.get('name') == game.team:
				game.teamRuns = child.getchildren()[0].get('R')
				game.teamHits = child.getchildren()[0].get('H')
				game.teamErrors = child.getchildren()[0].get('E')
			if child.tag == 'team' and child.get('name') != game.team:
				game.opponent = child.get('name')
				game.opponentRuns = child.getchildren()[0].get('R')
				game.opponentHits = child.getchildren()[0].get('H')
				game.opponentErrors = child.getchildren()[0].get('E')

		gameEventsRequest = requests.get(eventsUrl)
		# print(gameEventsRequest.text)
		gameEventsDocumentBytes = bytes(bytearray(gameEventsRequest.text, encoding='utf-8'))
		gameEventsDocumentXML = etree.XML(gameEventsDocumentBytes)
		
		# Get current/most recent inning
		inningRoot = gameEventsDocumentXML.xpath('/game/inning[last()]')[0]
		inning.number = inningRoot.get('num') or 0
		inning.half = (inningRoot.xpath("/game/inning[last()]/*[text() and string-length()>0][last()]")[0]).tag or ''
		atBatRoot = gameEventsDocumentXML.xpath("/game/inning[last()]/*[text() and string-length()>0][last()]/atbat[last()]")[0]
		atBatPlayerRoot = gameEventsDocumentXML.xpath("/game/atBat")[0]
		atBat.number = atBatRoot.get('num') or 0
		atBat.balls = atBatRoot.get('b') or 0
		atBat.strikes = atBatRoot.get('s') or 0
		atBat.outs = atBatRoot.get('o') or outs
		atBat.pitcher = getPlayer(players, atBatRoot.get('pitcher'))
		atBat.batter = getPlayer(players, atBatRoot.get('batter'))
		if atBatRoot.get('b1'):
			atBat.onFirst = getPlayer(players, atBatRoot.get('b1'))
		if atBatRoot.get('b2'):
			atBat.onSecond = getPlayer(players, atBatRoot.get('b2'))
		if atBatRoot.get('b3'):
			atBat.onThird = getPlayer(players, atBatRoot.get('b3'))
		atBat.description = atBatRoot.get('des') or ''
		atBat.guid = atBatRoot.get('play_guid') or ''
		trackAtBatID = atBat.number

		# Get current/most recent pitch of the inning
		pitchRoot = gameEventsDocumentXML.xpath("/game/inning[last()]/*[text() and string-length()>0][last()]/atbat[last()]/pitch[last()]")[0]
		pitch.id = pitchRoot.get('sv_id') or ''
		pitch.call = pitchRoot.get('type') or ''
		pitch.callDescription = pitchRoot.get('des') or ''
		pitch.speed = pitchRoot.get('start_speed') or 0
		pitch.pitchType = pitchRoot.get('pitch_type') or ''
		trackPitchID = pitch.id
		
		displayInGame(game, inning, atBat, pitch, interval)
	except Exception as ex:
		#print(ex)
		pass

	if game.status != 'FINAL':
		return True
	else:
		time.sleep(3600)
		return False
	
# ---------------------------------------------------------------------