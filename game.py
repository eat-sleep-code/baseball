import globals
import os
import pygame
import time
from data import Data
from utils import Image as imageUtils
from PIL import Image


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

		cellPadding = 10	
		columnLeftStart = 20
		columnRightStart = 400
		itemY = 20
		refreshCount = 0
		thumbnailWidth = 64
		thumbnailHeight = 64

		while globals.gameInProgress == True:
			# AWAY SCORE	
			item = Data.getCurrentPlay(globals.gameLink)   

			pygame.display.set_caption(globals.title + ' > ' + item.away.name + ' @ ' + item.home.name)
		
			awayLogoPath = imageUtils.webImage(item.away.logo)
			awayLogo = pygame.image.load(awayLogoPath)
			awayLogo = pygame.transform.smoothscale(awayLogo, (thumbnailWidth - (cellPadding*2), thumbnailHeight - (cellPadding*2)))
			globals.displaySurface.blit(awayLogo, (columnLeftStart, itemY + 20))
		
			awayScoreText = scoreFont.render(str(item.away.runs), True, (0, 0, 0))
			globals.displaySurface.blit(awayScoreText, (columnLeftStart, itemY + thumbnailHeight + 20 ))


			# HOME SCORE

			homeLogoPath = imageUtils.webImage(item.home.logo)
			homeLogo = pygame.image.load(homeLogoPath)
			homeLogo = pygame.transform.smoothscale(homeLogo, (thumbnailWidth - (cellPadding*2), thumbnailHeight - (cellPadding*2)))
			globals.displaySurface.blit(homeLogo, (columnRightStart, itemY + 20))
	
			homeScoreText = scoreFont.render(str(item.home.runs), True, (0, 0, 0))
			globals.displaySurface.blit(homeScoreText, (columnRightStart, itemY + thumbnailHeight + 20 ))
					
			
			print(item.status.description)

			pygame.display.flip()
			refreshCount += 1
			if refreshCount > 1:
				time.sleep(5)     
