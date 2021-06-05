import globals
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
        buttonWidth = 960
        buttonHeight = 100
        currentRow = 0
        currentColumn = 0

        buttonStyle = ttk.Style()
        buttonStyle.configure('default.TButton', background = '#FFFFFF', bordercolor = '#FFFFFF', borderwidth=0)
		

        for item in menuItems:
            self.canvas = tk.Canvas(self, width = 1920, height = 1080)
            self.canvas.pack()
            self.childFrame = tk.Frame(self.canvas, width=buttonWidth, height=buttonHeight)
            self.childFrame.grid(row=currentRow, column=currentColumn)
            print(currentRow, currentColumn)
            
            #sequentialId = item.sequentialId

# ---------------------------------------------------------------------

            self.awayLogo = imageUtils.webImage(item.away.logo)
            self.awayLogoImage = ImageTk.PhotoImage(Image.open(self.awayLogo))
            self.awayLogoButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.awayLogoImage, command=lambda link=item.link: selectGame(link))
            self.awayLogoButton['style'] = 'default.TButton'
            self.awayLogoButton.pack()
            self.awayLogoButton.place(x=0,y=0,width=120,height=120)
            
            self.awayNameButton = ttk.Button(self.childFrame, text=item.away.name, command=lambda link=item.link: selectGame(link))
            self.awayNameButton['style'] = 'default.TButton'
            self.awayNameButton.pack()
            self.awayNameButton.place(x=10,y=10,width=buttonWidth,height=buttonHeight)
            
            self.awayWinsButton = ttk.Button(self.childFrame, text=item.away.wins, command=lambda link=item.link: selectGame(link))
            self.awayWinsButton['style'] = 'default.TButton'
            self.awayWinsButton.pack()
            self.awayWinsButton.place(x=400,y=10,width=buttonWidth,height=buttonHeight)
            
            self.awayLossesButton = ttk.Button(self.childFrame, text=item.away.losses, command=lambda link=item.link: selectGame(link))
            self.awayLossesButton['style'] = 'default.TButton'
            self.awayLossesButton.pack()
            self.awayLossesButton.place(x=400,y=10,width=buttonWidth,height=buttonHeight)
            
# ---------------------------------------------------------------------

            self.homeLogo = imageUtils.webImage(item.home.logo)
            self.homeLogoImage = ImageTk.PhotoImage(Image.open(self.homeLogo))
            self.homeLogoButton = ttk.Button(self.childFrame, compound=tk.CENTER, image=self.homeLogoImage, command=lambda link=item.link: selectGame(link))
            self.homeLogoButton['style'] = 'default.TButton'
            self.homeLogoButton.pack()
            self.homeLogoButton.place(x=0,y=110,width=120,height=120)
            
            self.homeNameButton = ttk.Button(self.childFrame, text=item.home.name, command=lambda link=item.link: selectGame(link))
            self.homeNameButton['style'] = 'default.TButton'
            self.homeNameButton.pack()
            self.homeNameButton.place(x=10,y=120,width=buttonWidth,height=buttonHeight)
            
            self.homeWinsButton = ttk.Button(self.childFrame, text=item.home.wins, command=lambda link=item.link: selectGame(link))
            self.homeWinsButton['style'] = 'default.TButton'
            self.homeWinsButton.pack()
            self.homeWinsButton.place(x=400,y=120,width=buttonWidth,height=buttonHeight)
            
            self.homeLossesButton = ttk.Button(self.childFrame, text=item.home.losses, command=lambda link=item.link: selectGame(link))
            self.homeLossesButton['style'] = 'default.TButton'
            self.homeLossesButton.pack()
            self.homeLossesButton.place(x=400,y=120,width=buttonWidth,height=buttonHeight)
            
# ---------------------------------------------------------------------
            
            self.timezoneButton = ttk.Button(self.childFrame, text=item.time + ' ' + str(item.timezone), command=lambda link=item.link: selectGame(link))
            self.timezoneButton['style'] = 'default.TButton'
            self.timezoneButton.pack()
            #self.homeLossesButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)
            
# ---------------------------------------------------------------------
                    
            self.childFrame.bind("<Return>", lambda event, link=item.link: selectGame(link))
            self.childFrame.focus_set()

            
            
            # Set position of next button...
            if currentColumn == 0:
                currentColumn = 1
            else: 
                currentColumn = 0
                currentRow += 1
            

            #if (x + buttonWidth) == buttonWidth:
            #    x = x * 2
            #else:
            #    x = 0
            #y = y + buttonHeight


        def selectGame(link):
            globals.gamesSelected = True
            print(globals.gamesSelected)
            print('Clicked: ' + link)