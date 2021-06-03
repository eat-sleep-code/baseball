from papirus import PapirusTextPos

display = PapirusTextPos(False)
minX = 0
minY = 0



def writeToDisplay(text = '', x=2, y=2, size=14, id='Default', fontPath=fontPath, maxLines=100):
	display.AddText(text=text, x=x, y=y, size=size, Id=id, invert=False, fontPath=fontPath, maxLines=maxLines)
	#print(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S %Z') + ': ' + text)
	#print('')
	return

# ---------------------------------------------------------------------


# ---------------------------------------------------------------------

def displayBoxScore(game, inning):
	display.Clear()
	if game.status == 'FINAL': 
		writeToDisplay('FINAL', minX, minY, 14, 'BoxScoreInning', fontPath)
	else: 
		writeToDisplay(inning.half + ' ' + number.ordinal(inning.number), minX, minY, 14, 'BoxScoreInning', fontPath)

	writeToDisplay('R', 125, 35, 14, 'RunsHeader', fontPath)
	writeToDisplay('H', 150, 35, 14, 'HitsHeader', fontPath)
	writeToDisplay('E', 175, 35, 14, 'ErrorsHeader', fontPath)
	
	writeToDisplay(game.team, minX, 55, 14, 'Team', fontPath)
	writeToDisplay(game.teamRuns, 125, 55, 14, 'TeamRuns', fontPath)
	writeToDisplay(game.teamHits, 150, 55, 14, 'TeamHits', fontPath)
	writeToDisplay(game.teamErrors, 175, 55, 14, 'TeamErrors', fontPath)
	
	writeToDisplay(game.opponent, minX, 75, 14, 'Opponent', fontPath)
	writeToDisplay(game.opponentRuns, 125, 75, 14, 'OpponentRuns', fontPath)
	writeToDisplay(game.opponentHits, 150, 75, 14, 'OpponentHits', fontPath)
	writeToDisplay(game.opponentErrors, 175, 75, 14, 'OpponentErrors', fontPath)
	
	display.WriteAll(partialUpdate=True)
	return

# ---------------------------------------------------------------------

def displayPitch(game, atBat, pitch):
	display.Clear()
	writeToDisplay(getAtBatTeam(game, atBat), minX, minY, 14, 'Versus', fontPath)
	
	writeToDisplay('Pitcher: ' + atBat.pitcher.first + ' ' + atBat.pitcher.last, minX, 20, 12, 'Pitcher', fontPath)
	writeToDisplay(str(atBat.pitcher.era) + ' ' + 'ERA', 150, 22, 10, 'PitcherStats', fontPath)
	writeToDisplay(str(pitch.speed) + ' MPH ' + getPitchType(pitch), minX, 35, 10, 'Pitch', fontPath)
	writeToDisplay('At Bat: ' + atBat.batter.first + ' ' + atBat.batter.last, minX, 50, 12, 'Batter', fontPath)
	writeToDisplay('#' + str(atBat.batter.number) + ' ' + atBat.batter.position, 150, 52, 10, 'BatterPosition', fontPath)
	writeToDisplay(str(atBat.batter.avg) + 'AVG, ' + str(atBat.batter.hr) + ' HR', minX, 65, 10, 'BatterStats', fontPath)
	writeToDisplay(pitch.callDescription, minX, 80, 10, 'Call', fontPath)
	display.WriteAll(partialUpdate=True)
	return

# ---------------------------------------------------------------------

def displayPlay(game, atBat, pitch):
	baseDefault = u"\u25C7"
	baseHighlight = u"\u25C6"
	
	display.Clear()
	writeToDisplay(getAtBatTeam(game, atBat), minX, minY, 14, 'Versus', fontPath)
	writeToDisplay(atBat.description, minX, 17, 10, 'Description', maxLines=3)

	writeToDisplay('B', minX, 50, 12, 'BallsLabel', fontPath)
	writeToDisplay(getCount(atBat.balls, 4), 25, 50, 12, 'BallsCount', dingsPath)
	writeToDisplay('S', minX, 65, 12, 'StrikesLabel', fontPath)
	writeToDisplay(getCount(atBat.strikes, 3), 25, 65, 12, 'StrikesCount', dingsPath)
	writeToDisplay('O', minX, 80, 12, 'OutsLabel', fontPath)
	writeToDisplay(getCount(atBat.outs, 3), 25, 80, 12, 'OutsCount', dingsPath)
	
	if atBat.onFirst is not None:
		writeToDisplay(baseHighlight, 170, 70, 20, 'FirstBase', dingsPath)
	else:
		writeToDisplay(baseDefault, 170, 70, 20, 'FirstBase', dingsPath)
	
	if atBat.onSecond is not None:
		writeToDisplay(baseHighlight, 150, 55, 20, 'SecondBase', dingsPath)
	else:
		writeToDisplay(baseDefault, 150, 55, 20, 'SecondBase', dingsPath)
	
	if atBat.onThird is not None:
		writeToDisplay(baseHighlight, 130, 70, 20, 'ThirdBase', dingsPath)
	else:
		writeToDisplay(baseDefault, 130, 70, 20, 'ThirdBase', dingsPath)
	display.WriteAll(partialUpdate=True)
	return
	
# ---------------------------------------------------------------------

def displayInGame(game, inning, atBat, pitch, interval):
	if game.status == 'FINAL':
		displayBoxScore(game, inning)
		time.sleep(interval)
	elif game.status == 'PREGAME':
		displayStatus('Game starting soon!', interval)
	else:
		displayBoxScore(game, inning)
		time.sleep(interval/3)
		displayPitch(game, atBat, pitch)
		time.sleep(interval/3)
		displayPlay(game, atBat, pitch)
		time.sleep(interval/3)
	return 

# ---------------------------------------------------------------------

def displayStatus(message, wait):
	display.Clear()
	writeToDisplay(message, minX, minY, 14, 'Status', fontPath)
	display.WriteAll()
	time.sleep(wait)
	return 

# --------------------------------------------------------------------
