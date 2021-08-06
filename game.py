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
		columnLeftStart = 50
		columnRightStart = 1600
		itemY = 20
		refreshCount = 0
		thumbnailWidth = 64
		thumbnailHeight = 64

		while globals.gameInProgress == True:
			item = Data.getCurrentPlay(globals.gameLink)   
			pygame.display.set_caption(globals.title + ' > ' + item.away.name + ' @ ' + item.home.name)
			


			# =================================================================



			# AWAY SCORE
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
				
		

			# =================================================================



			if currentPlay.inningHalf == 'bottom':
				columnPitchingStart = columnRightStart
				columnBattingStart = columnLeftStart
			else:
				columnPitchingStart = columnLeftStart
				columnBattingStart = columnRightStart


			# PITCHING
			pitcherNameText = defaultFont.render(str(item.pitcher.name), True, (0, 0, 0))
			globals.displaySurface.blit(pitcherNameText, (columnPitchingStart, itemY + thumbnailHeight + 60 ))
			
			pitcherPortraitPath = imageUtils.webImage(item.pitcher.portrait, 'player-' + str(item.pitcher.playerId))
			pitcherPortrait = pygame.image.load(pitcherPortraitPath)
			globals.displaySurface.blit(pitcherPortrait, (columnPitchingStart, itemY + thumbnailHeight + 80 ))
			
			pitcherPitchesText = defaultFont.render(str(item.pitcher.pitches), True, (0, 0, 0))
			globals.displaySurface.blit(pitcherPitchesText, (columnPitchingStart, itemY + thumbnailHeight + 400 ))
			

			# BATTING
			batterNameText = defaultFont.render(str(item.batter.name), True, (0, 0, 0))
			globals.displaySurface.blit(batterNameText, (columnBattingStart, itemY + thumbnailHeight + 60 ))
			
			batterPortraitPath = imageUtils.webImage(item.batter.portrait, 'player-' + str(item.batter.playerId))
			batterPortrait = pygame.image.load(batterPortraitPath)
			globals.displaySurface.blit(batterPortrait, (columnBattingStart, itemY + thumbnailHeight + 80 ))
			
			batterBatsText = defaultFont.render(str(item.batter.bats), True, (0, 0, 0))
			globals.displaySurface.blit(batterBatsText, (columnBattingStart, itemY + thumbnailHeight + 400 ))
			


			# =================================================================



			print(item.status.description)

			pygame.display.flip()
			refreshCount += 1
			if refreshCount > 1:
				time.sleep(5)     
