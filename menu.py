import globals
import os
import pygame
import time
from data import Data
from utils import Image as imageUtils
from PIL import Image

class CreateMenu:
	def __init__(self):
		
		
		pygame.display.set_caption(globals.title + ' > Today\'s Games')
		
		displayWidth, displayHeight = pygame.display.get_surface().get_size()
		#menuItemsSurface = pygame.Surface((int(displayWidth), int(displayHeight)))

# ---------------------------------------------------------------------
		
		defaultFont = pygame.font.SysFont('Helvetica', 16, bold=False)
		teamNameFont = pygame.font.SysFont('Helvetica', 18, bold=True)
		scoreFont = pygame.font.SysFont('Helvetica', 30, bold=True)
		
	
# ---------------------------------------------------------------------		
		
		while globals.gameSelected == False: 
			
			backgroundImagePath = os.path.join(globals.homePath, 'images/menu-background.jpg')
			backgroundImage = pygame.image.load(backgroundImagePath)
			globals.displaySurface.blit(backgroundImage, (0, 0))

			# ---------------------------------------------------------------------

			padding = 72
			x = padding
			y = padding 
			desiredColumns = 3
			thumbnailWidth = 64
			thumbnailHeight = 64
			cellPadding = 10
			buttonWidth = int(((globals.screenWidth - x) / desiredColumns) - y) 
			buttonHeight = int(thumbnailHeight * 2)
			teamTextWidth = 256
			scoreTextWidth = 100

			# ---------------------------------------------------------------------
			
			menuItems = Data.getSchedule().games
			if len(menuItems) == 0:
				print('Awaiting game data...')
			else:
				if len(menuItems) > 12:
					y = y/2
				for item in menuItems:
					itemX = x
					itemY = y
					itemYAlt = y + thumbnailHeight

					gameRectangle = pygame.draw.rect(globals.displaySurface, (255, 255, 255), [itemX, itemY, buttonWidth, buttonHeight])
					#for event in pygame.event.get():
						#if event.type == 1:
							#print(pygame.mouse.get_pos())
							#if gameRectangle.collidepoint():
							#	print('Clicked', item.away.name)
					
					

					# ---------------------------------------------------------------------

					columnStart = itemX + cellPadding + 6

					awayLogoPath = imageUtils.webImage(item.away.logo)
					awayLogo = pygame.image.load(awayLogoPath)
					awayLogo = pygame.transform.smoothscale(awayLogo, (thumbnailWidth - (cellPadding*2), thumbnailHeight - (cellPadding*2)))
					globals.displaySurface.blit(awayLogo, (columnStart, itemY + cellPadding))

					homeLogoPath = imageUtils.webImage(item.home.logo)
					homeLogo = pygame.image.load(homeLogoPath)
					homeLogo = pygame.transform.smoothscale(homeLogo, (thumbnailWidth - (cellPadding*2), thumbnailHeight - (cellPadding*2)))
					globals.displaySurface.blit(homeLogo, (columnStart, itemYAlt + cellPadding))
					
					# ---------------------------------------------------------------------
					
					columnStart = itemX + thumbnailWidth + cellPadding + 6

					awayText = teamNameFont.render(item.away.name, True, (0, 0, 0))
					globals.displaySurface.blit(awayText, (columnStart, itemY + 20))

					homeText = teamNameFont.render(item.home.name, True, (0, 0, 0))
					globals.displaySurface.blit(homeText, (columnStart, itemYAlt + 20 ))

					# ---------------------------------------------------------------------
					
					columnStart = itemX + thumbnailWidth + teamTextWidth

					if item.status.code == 'I' or item.status.code == 'F':
						awayScoreText = scoreFont.render(str(item.away.runs), True, (0, 0, 0))
						globals.displaySurface.blit(awayScoreText, (columnStart, itemY + 14 ))

						homeScoreText = scoreFont.render(str(item.home.runs), True, (0, 0, 0))
						globals.displaySurface.blit(homeScoreText, (columnStart, itemYAlt + 14 ))
					else:
						awayWinLossText = defaultFont.render(str(item.away.wins) + ' - ' + str(item.away.losses), True, (128, 128, 128))
						globals.displaySurface.blit(awayWinLossText, (columnStart, itemY + 22 ))

						homeWinLossText = defaultFont.render(str(item.home.wins) + ' - ' + str(item.home.losses), True, (128, 128, 128))
						globals.displaySurface.blit(homeWinLossText, (columnStart, itemYAlt + 22 ))
					
					# ---------------------------------------------------------------------
						
					columnStart = itemX + thumbnailWidth + teamTextWidth + scoreTextWidth

					if item.status.code == 'F':
						# FINAL Indicator
						finalText = scoreFont.render('Final', True, (0, 0, 0))
						globals.displaySurface.blit(finalText, (columnStart, itemYAlt - 10 ))
					elif item.status.code == 'I':
						
						# Base Pattern
						
						basePatternImagePath = os.path.join(globals.homePath, 'images/bases/', item.basePattern + '.png')
						basePatternImage = pygame.image.load(basePatternImagePath)
						basePatternImage = pygame.transform.smoothscale(basePatternImage, (90, 60))
						globals.displaySurface.blit(basePatternImage, (columnStart, itemY + 10))

						# Inning
						if (item.inningHalf == 'top'):
							inningIndicator = u"\u25B2 " + str(item.inning)
						elif (item.inningHalf == 'bottom'):
							inningIndicator = u"\u25BC " + str(item.inning)
						else:
							inningIndicator = u"\u2013 " + str(item.inning)

						inningText = defaultFont.render(inningIndicator, True, (0, 0, 0))
						globals.displaySurface.blit(inningText, (columnStart + 33, itemY + 65 ))
						
					
						# Outs
						outImagePath = os.path.join(globals.homePath, 'images/outs/', str(item.outs) + '.png')
						outImage = pygame.image.load(outImagePath)
						outImage = pygame.transform.smoothscale(outImage, (90, 30))
						globals.displaySurface.blit(outImage, (columnStart, itemY + 88))
			
					else:
						# Start Time
						startTimeText = defaultFont.render(item.time + ' ' + str(item.timezone), True, (0, 0, 0))
						globals.displaySurface.blit(startTimeText, (columnStart, itemYAlt - 10 ))


					if (x >= buttonWidth * (desiredColumns - 1)):	
						x = padding
						y = itemY + buttonHeight + padding
					else:
						x = itemX + buttonWidth + padding
					#print('X:', x, 'Y:', y)

				pygame.display.flip()
				time.sleep(5)		
				

# ---------------------------------------------------------------------

		def menuButton(item, x, y, w, h, action=None):
			mousePositon = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed() 
			print(click)

# ---------------------------------------------------------------------

		def selectGame(link):
			globals.gamesSelected = True
			print(globals.gamesSelected)
			print('Clicked: ' + link)