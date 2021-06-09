import os
import pygame

def initialize():
	pygame.init()
	
	global title
	title = 'Baseball'
	
	global pollRate
	pollRate = 10
	
	global screenWidth
	screenWidth = 1920

	global screenHeight
	screenHeight = 1080

	global displaySurface
	displaySurface = pygame.display.set_mode((0,0), pygame.HWSURFACE | pygame.DOUBLEBUF)

	#--------------------------------------------------------------------------
		
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
	
	