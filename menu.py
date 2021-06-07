import globals
import os
from data import Data
from utils import Image as imageUtils
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CreateMenu(tk.Canvas):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		menuItems = Data.getSchedule().games
		self.tk_images = []

# ---------------------------------------------------------------------

		padding = 72
		x = padding
		y = padding 
		desiredColumns = 3
		thumbnailWidth = 64
		thumbnailHeight = 64
		buttonWidth = (globals.screenWidth - padding) / desiredColumns 
		buttonHeight = thumbnailHeight * 2
		buttonBorder = 1
		teamTextWidth = 256
		scoreTextWidth = 100
		gameStatusTextWidth = 100

# ---------------------------------------------------------------------
		
		buttonStyle = ttk.Style()
		buttonStyle.configure('bold.TButton', foreground='#000000', background = '#FFFFFF', bordercolor = '#FFFFFF', borderwidth=0, font=('Helvetica', 16, 'bold'))	
		buttonStyle.configure('light.TButton', foreground='#888888', background = '#FFFFFF', bordercolor = '#FFFFFF', color='#888888', borderwidth=0, font=('Helvetica', 12))	
		buttonStyle.configure('default.TButton', foreground='#000000', background = '#FFFFFF', bordercolor = '#FFFFFF', borderwidth=0, font=('Helvetica', 12))	
		buttonStyle.configure('score.TButton', foreground='#000000', background = '#FFFFFF', bordercolor = '#FFFFFF', borderwidth=0, font=('Helvetica', 20, 'bold'))	
		buttonStyle.map('default.Tbutton', background=[('!active', '#FFFFFF')])
	
# ---------------------------------------------------------------------

		self.canvas = tk.Canvas(self, bg = '#000000', width = globals.screenWidth, height = globals.screenHeight)
		self.image = Image.open(os.path.join(globals.homePath, 'images/menu-background.jpg'))
		self.splashScreenImage = ImageTk.PhotoImage(self.image)
		self.canvas.create_image(0, 0, anchor='nw', image=self.splashScreenImage)
		self.canvas.pack()
			
		for item in menuItems:
			self.childFrame = tk.Frame(self.canvas, width=(buttonWidth - padding), height=buttonHeight, bg='#888888')

# ---------------------------------------------------------------------

			self.awayLogo = imageUtils.webImage(item.away.logo)
			self.awayLogoImageFile = Image.open(self.awayLogo)
			self.awayLogoImageFile = self.awayLogoImageFile.resize((thumbnailWidth - 20, thumbnailHeight - 20), Image.ANTIALIAS) 
			self.awayLogoImage = ImageTk.PhotoImage(self.awayLogoImageFile, format='png', width=thumbnailWidth, height=thumbnailHeight)
			self.awayLogoButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.awayLogoImage, command=lambda link=item.link: selectGame(link))
			self.awayLogoButton['style'] = 'default.TButton'
			self.awayLogoButton.place(x=0, y=0, width=thumbnailWidth, height=thumbnailHeight)
			self.tk_images.append(self.awayLogoImage)

			self.awayNameButton = ttk.Button(self.childFrame, text=item.away.name, command=lambda link=item.link: selectGame(link))
			self.awayNameButton['style'] = 'bold.TButton'
			self.awayNameButton.place(x=thumbnailWidth, y=0, height=buttonHeight/2, width=teamTextWidth)
			
			
# ---------------------------------------------------------------------

			self.homeLogo = imageUtils.webImage(item.home.logo)
			self.homeLogoImageFile = Image.open(self.homeLogo)
			self.homeLogoImageFile = self.homeLogoImageFile.resize((thumbnailWidth - 16, thumbnailHeight - 16), Image.ANTIALIAS) 
			self.homeLogoImage = ImageTk.PhotoImage(self.homeLogoImageFile, format='png', width=thumbnailWidth, height=thumbnailHeight)
			self.homeLogoButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.homeLogoImage, command=lambda link=item.link: selectGame(link))
			self.homeLogoButton['style'] = 'default.TButton'
			self.homeLogoButton.place(x=0, y=thumbnailHeight, width=thumbnailWidth, height=thumbnailHeight)
			self.tk_images.append(self.homeLogoImage)

			self.homeNameButton = ttk.Button(self.childFrame, text=item.home.name, command=lambda link=item.link: selectGame(link))
			self.homeNameButton['style'] = 'bold.TButton'
			self.homeNameButton.place(x=thumbnailWidth, y=thumbnailHeight, height=buttonHeight/2, width=teamTextWidth)

# ---------------------------------------------------------------------	
			
			if item.status.code == 'I' or item.status.code == 'F':
				self.awayScoreButton = ttk.Button(self.childFrame, text=str(item.away.runs), command=lambda link=item.link: selectGame(link))
				self.awayScoreButton['style'] = 'score.TButton'
				self.awayScoreButton.place(x=thumbnailWidth + teamTextWidth, y=0, height=buttonHeight/2, width = scoreTextWidth)
				
				self.homeScoreButton = ttk.Button(self.childFrame, text=str(item.home.runs), command=lambda link=item.link: selectGame(link))
				self.homeScoreButton['style'] = 'score.TButton'
				self.homeScoreButton.place(x=thumbnailWidth + teamTextWidth, y=thumbnailHeight, height=buttonHeight/2, width = scoreTextWidth)
				
			else:
				self.awayWinLossButton = ttk.Button(self.childFrame, text=str(item.away.wins) + ' - ' + str(item.away.losses), command=lambda link=item.link: selectGame(link))
				self.awayWinLossButton['style'] = 'light.TButton'
				self.awayWinLossButton.place(x=thumbnailWidth + teamTextWidth, y=0, height=buttonHeight/2, width = scoreTextWidth)
				
				self.homeWinLossButton = ttk.Button(self.childFrame, text=str(item.home.wins) + ' - ' + str(item.home.losses), command=lambda link=item.link: selectGame(link))
				self.homeWinLossButton['style'] = 'light.TButton'
				self.homeWinLossButton.place(x=thumbnailWidth + teamTextWidth, y=thumbnailHeight, height=buttonHeight/2, width = scoreTextWidth)
				
# ---------------------------------------------------------------------
			
			if item.status.code == 'F':
				# FINAL Indicator
				self.gameStatusButton = ttk.Button(self.childFrame, text='Final', command=lambda link=item.link: selectGame(link))
				self.gameStatusButton['style'] = 'default.TButton'
				self.gameStatusButton.place(x=thumbnailWidth + teamTextWidth + scoreTextWidth + 1, y=0, height=buttonHeight, width=(buttonWidth - thumbnailWidth - teamTextWidth - scoreTextWidth - padding - 1))
			elif item.status.code == 'I':
				# Inning
				if (item.inningHalf == 'bottom'):
					inningIndicator = u"\u25B2 " + str(item.inning)
				else:
					inningIndicator = u"\u25BC " + str(item.inning)
				self.gameStatusButton = ttk.Button(self.childFrame, text=inningIndicator, command=lambda link=item.link: selectGame(link))
				self.gameStatusButton['style'] = 'default.TButton'
				self.gameStatusButton.place(x=thumbnailWidth + teamTextWidth + scoreTextWidth + 1, y=0, height=buttonHeight/3, width=(buttonWidth - thumbnailWidth - teamTextWidth - scoreTextWidth - padding - 1))
				
				# Base Pattern
				self.basePatternImage = ImageTk.PhotoImage(os.path.join(globals.homePath, 'images/bases/', item.basePattern, '.png'), format='png', width=thumbnailWidth, height=thumbnailHeight)
				self.basePatternButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.basePatternImage, command=lambda link=item.link: selectGame(link))
				self.basePatternButton['style'] = 'default.TButton'
				self.basePatternButton.place(x=0, y=buttonHeight/3, width=thumbnailWidth, height=thumbnailHeight)
				self.tk_images.append(self.basePatternImage)

				# Outs
				self.outImage = ImageTk.PhotoImage(os.path.join(globals.homePath, 'images/outs/', str(item.outs), '.png'), format='png', width=thumbnailWidth, height=thumbnailHeight)
				self.outButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.outImage, command=lambda link=item.link: selectGame(link))
				self.outButton['style'] = 'default.TButton'
				self.outButton.place(x=0, y=buttonHeight/3, width=thumbnailWidth, height=thumbnailHeight)
				self.tk_images.append(self.outButton)
			else:
				# Standings
				self.gameStatusButton = ttk.Button(self.childFrame, text=item.time + ' ' + str(item.timezone), command=lambda link=item.link: selectGame(link))
				self.gameStatusButton['style'] = 'default.TButton'
				self.gameStatusButton.place(x=thumbnailWidth + teamTextWidth + scoreTextWidth + 1, y=0, height=buttonHeight, width=(buttonWidth - thumbnailWidth - teamTextWidth - scoreTextWidth - padding - 1))
			
# ---------------------------------------------------------------------
					
				
				
			self.childFrame.bind("<Return>", lambda event, link=item.link: selectGame(link))
			self.childFrame.focus_set()

			self.childFrame.place(x = x, y = y)
			
			if (x == (globals.screenWidth - buttonWidth)):
				x = 0
				y = y + buttonHeight
			else:
				x = x + buttonWidth
			#print(x, y)
			

		def selectGame(link):
			globals.gamesSelected = True
			print(globals.gamesSelected)
			print('Clicked: ' + link)