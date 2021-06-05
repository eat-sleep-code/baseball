import globals
from data import Data
from utils import Image as imageUtils
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CreateMenu(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #self.bind('Click')
        
        menuItems = Data.getSchedule().games
        x = 0 
        y = 0
        buttonWidth = 960
        buttonHeight = 100

        buttonStyle = ttk.Style()
        buttonStyle.configure('default.TButton', background = '#222222', bordercolor = '#111111', borderwidth=0)
		

        for item in menuItems:
            self.frame = tk.Frame(self)
            self.frame.pack()
        
            #sequentialId = item.sequentialId

# ---------------------------------------------------------------------

            awayLogo = Image.open(imageUtils.SVGtoPNG(item.away.logo))
            awayLogoImage = ImageTk.PhotoImage(awayLogo)
            awayLogoButton = ttk.Button(root, compound=tk.CENTER, image=awayLogoImage, command=lambda link=item.link: selectGame(link))
            awayLogoButton['style'] = 'default.TButton'
            #awayLogoButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)
            
            self.awayNameButton = ttk.Button(self.frame, text=item.away.name, command=lambda link=item.link: selectGame(link))
            self.awayNameButton['style'] = 'default.TButton'
            self.awayNameButton.pack()
            #self.awayNameButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)

            self.awayWinsButton = ttk.Button(self.frame, text=item.away.wins, command=lambda link=item.link: selectGame(link))
            self.awayWinsButton['style'] = 'default.TButton'
            self.awayWinsButton.pack()
            #self.awayWinsButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)

            self.awayLossesButton = ttk.Button(self.frame, text=item.away.losses, command=lambda link=item.link: selectGame(link))
            self.awayLossesButton['style'] = 'default.TButton'
            self.awayLossesButton.pack()
            #self.awayLossesButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)

# ---------------------------------------------------------------------

            homeLogo = Image.open(imageUtils.SVGtoPNG(item.home.logo))
            homeLogoImage = ImageTk.PhotoImage(homeLogo)
            homeLogoButton = ttk.Button(root, compound=tk.CENTER, image=homeLogoImage, command=lambda link=item.link: selectGame(link))
            homeLogoButton['style'] = 'default.TButton'
            #homeLogoButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)
            
            self.homeNameButton = ttk.Button(self.frame, text=item.home.name, command=lambda link=item.link: selectGame(link))
            self.homeNameButton['style'] = 'default.TButton'
            self.homeNameButton.pack()
            #self.homeNameButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)

            self.homeWinsButton = ttk.Button(self.frame, text=item.home.wins, command=lambda link=item.link: selectGame(link))
            self.homeWinsButton['style'] = 'default.TButton'
            self.homeWinsButton.pack()
            #self.homeWinsButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)

            self.homeLossesButton = ttk.Button(self.frame, text=item.home.losses, command=lambda link=item.link: selectGame(link))
            self.homeLossesButton['style'] = 'default.TButton'
            self.homeLossesButton.pack()
            #self.homeLossesButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)

# ---------------------------------------------------------------------
            
            self.timezoneButton = ttk.Button(self.frame, text=item.time + ' ' + str(item.timezone), command=lambda link=item.link: selectGame(link))
            self.timezoneButton['style'] = 'default.TButton'
            self.timezoneButton.pack()
            #self.homeLossesButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)

# ---------------------------------------------------------------------
                    
            self.frame.bind("<Return>", lambda event, link=item.link: selectGame(link))
            self.frame.focus_set()

            
            
            #print('\n----------\n')

            # Set position of next button...
            #if (x + buttonWidth) == buttonWidth:
            #    x = x * 2
            #else:
            #    x = 0
            #y = y + buttonHeight


        def selectGame(link):
            globals.gamesSelected = True
            print(globals.gamesSelected)
            print('Clicked: ' + link)