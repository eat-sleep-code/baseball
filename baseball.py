#!/usr/bin/python3
import globals
import os
import pygame
import sys
import threading
import time

from utils import Image as imageUtils
from game import ViewGame
from menu import CreateMenu
from display import Clear, ShowSplash


#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV', '/dev/fb1')
#os.putenv('SDL_MOUSEDRV', 'TSLIB')
#os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

#--------------------------------------------------------------------------

def buttonHandler():
	while True:
		#print('Buttons: ', len(globals.buttonCollection))
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in globals.buttonCollection:
					rect = button.rect
					if rect.collidepoint(event.pos):
						if button.type == 'schedule' and button.active == True:
							globals.gameInProgress = True
							globals.gameSelected = True
							globals.gameLink = button.value
				

#--------------------------------------------------------------------------

def playBall():
	try:
		globals.initialize()
			
		if globals.splashDisplayed == False:
			imageUtils.emptyCache()
			showSplash = ShowSplash()
			globals.splashDisplayed = True
			time.sleep(5)

		buttonHandlerThread = threading.Thread(target=buttonHandler)
		buttonHandlerThread.start()
		while True:
			if globals.gameSelected == True and globals.gameInProgress == True:
				showGame = ViewGame()
			else:
				menu = CreateMenu()
		
	except KeyboardInterrupt:
		sys.exit(1)
		
#--------------------------------------------------------------------------

playBall()

