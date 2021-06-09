import globals
import os
import pygame
import time
from data import Data

class ViewGame():
	def __init__(self):

		
		displayWidth, displayHeight = pygame.display.get_surface().get_size()
		
		backgroundImagePath = os.path.join(globals.homePath, 'images/in-game-background.jpg')
		backgroundImage = pygame.image.load(backgroundImagePath)
		globals.displaySurface.blit(backgroundImage, (0, 0))

# ---------------------------------------------------------------------
		
		defaultFont = pygame.font.SysFont('Helvetica', 16, bold=False)
		teamNameFont = pygame.font.SysFont('Helvetica', 18, bold=True)
		scoreFont = pygame.font.SysFont('Helvetica', 30, bold=True)
		
# ---------------------------------------------------------------------

		refreshCount = 0
		while globals.gameInProgress == True:	
			current = Data.getCurrentPlay(globals.gameLink)   

			pygame.display.set_caption(globals.title + ' > ' + current.away.name + ' @ ' + current.home.name)
		
			
			print(current.status.description)

			pygame.display.flip()
			refreshCount += 1
			if refreshCount > 1:
				time.sleep(5)     
