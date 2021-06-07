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
		
		#self.bind('Click')
		
		menuItems = Data.getSchedule().games
		x = 0 
		y = 0
		desiredColumns = 3
		buttonWidth = globals.screenWidth / desiredColumns
		buttonHeight = 100
		buttonBorder = 1
		thumbnailWidth = 50
		thumbnailHeight = 50
		
		buttonStyle = ttk.Style()
		buttonStyle.configure('default.TButton', background = '#FFFFFF', bordercolor = '#FFFFFF', borderwidth=0, font=('Helvetica', 14))	
	
		self.canvas = tk.Canvas(self, bg = '#00DD00', width = globals.screenWidth, height = globals.screenHeight)
		self.image = Image.open(os.path.join(globals.homePath, 'images/menu-background.jpg'))
		self.splashScreenImage = ImageTk.PhotoImage(self.image)
		self.canvas.create_image(0, 0, anchor='nw', image=self.splashScreenImage)
		self.canvas.pack()
			
		for item in menuItems:
			self.childFrame = tk.Frame(self.canvas, width=buttonWidth - 1, height=buttonHeight, bg='#FF0000')
			#self.childFrame.grid(row=currentRow, column=currentColumn)
			#print(currentRow, currentColumn)
			
			#sequentialId = item.sequentialId

# ---------------------------------------------------------------------
			self.awayLogo = imageUtils.webImage(item.away.logo)
			print(self.awayLogo)
			self.awayLogoImage = ImageTk.PhotoImage(Image.open(self.awayLogo), format='png', width=thumbnailWidth, height=thumbnailHeight)
			self.awayLogoButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.awayLogoImage, command=lambda link=item.link: selectGame(link))
			self.awayLogoButton.pack()
			self.awayLogoButton.place(x=0,y=0,width=thumbnailWidth,height=thumbnailHeight)
			
			self.awayNameButton = ttk.Button(self.childFrame, text=item.away.name, command=lambda link=item.link: selectGame(link))
			self.awayNameButton['style'] = 'default.TButton'
			self.awayNameButton.pack()
			self.awayNameButton.place(x=thumbnailWidth + 30,y=0,height=buttonHeight/2)
			
			self.awayWinLossButton = ttk.Button(self.childFrame, text=str(item.away.wins) + ' - ' + str(item.away.losses), command=lambda link=item.link: selectGame(link))
			self.awayWinLossButton['style'] = 'default.TButton'
			self.awayWinLossButton.pack()
			self.awayWinLossButton.place(x=thumbnailWidth + 230,y=0,height=buttonHeight/2)
			
# ---------------------------------------------------------------------

			self.homeLogo = imageUtils.webImage(item.home.logo)
			print(self.homeLogo)
			self.homeLogoImage = ImageTk.PhotoImage(Image.open(self.homeLogo), format='png', width=thumbnailWidth, height=thumbnailHeight)
			self.homeLogoButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.homeLogoImage, command=lambda link=item.link: selectGame(link))
			self.homeLogoButton.pack()
			self.homeLogoButton.place(x=0,y=thumbnailHeight,width=thumbnailWidth,height=thumbnailHeight)
			
			self.homeNameButton = ttk.Button(self.childFrame, text=item.home.name, command=lambda link=item.link: selectGame(link))
			self.homeNameButton['style'] = 'default.TButton'
			self.homeNameButton.pack()
			self.homeNameButton.place(x=thumbnailWidth + 30,y=thumbnailHeight,height=buttonHeight/2)
			
			self.homeWinLossButton = ttk.Button(self.childFrame, text=str(item.home.wins) + ' - ' + str(item.home.losses), command=lambda link=item.link: selectGame(link))
			self.homeWinLossButton['style'] = 'default.TButton'
			self.homeWinLossButton.pack()
			self.homeWinLossButton.place(x=thumbnailWidth + 230,y=thumbnailHeight,height=buttonHeight/2)
			
	
			
# ---------------------------------------------------------------------
			
			self.startTimeButton = ttk.Button(self.childFrame, text=item.time + ' ' + str(item.timezone), command=lambda link=item.link: selectGame(link))
			self.startTimeButton['style'] = 'default.TButton'
			self.startTimeButton.pack()
			self.startTimeButton.place(x=thumbnailWidth + 350,y=0,height=buttonHeight)
			
# ---------------------------------------------------------------------
					
			self.childFrame.bind("<Return>", lambda event, link=item.link: selectGame(link))
			self.childFrame.focus_set()

			self.childFrame.pack(ipady = 1)
			self.childFrame.place(x = x, y = y)
			
			if (x == (globals.screenWidth - buttonWidth)):
				x = 0
				y = y + buttonHeight + 1
			else:
				x = x + buttonWidth
			#print(x, y)
			

		def selectGame(link):
			globals.gamesSelected = True
			print(globals.gamesSelected)
			print('Clicked: ' + link)