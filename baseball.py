#!/usr/bin/python3
import globals
import os
import pygame
import sys
import time

from utils import Image as imageUtils
from game import Game
from menu import CreateMenu
from display import Clear, ShowSplash


#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV', '/dev/fb1')
#os.putenv('SDL_MOUSEDRV', 'TSLIB')
#os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

def PlayBall():
	try:
		globals.initialize()
			
		if globals.splashDisplayed == False:
			imageUtils.emptyCache()
			showSplash = ShowSplash()
			globals.splashDisplayed = True
			time.sleep(5)

		while True:
			if globals.gameSelected == True and globals.gameInProgress == True:
				print('Showing Game')
				#showGame = Game(canvas).getCurrentPlay()
			else:
				menu = CreateMenu()
		
	except KeyboardInterrupt:
		sys.exit(1)
		

playBall = PlayBall()

