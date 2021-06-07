import os
from pathlib import Path

def initialize():
	global homePath
	homePath = '/home/pi/source/baseball'
	os.chdir(homePath)

	global splashDisplayed
	splashDisplayed = False
	
	global gameSelected
	gameSelected = False

	global gameInProgress
	gameInProgress = False

	global imageCache
	imageCache = str(homePath + '/images/cache/')
	
	global screenWidth
	screenWidth = 1920

	global screenHeight
	screenHeight = 1080