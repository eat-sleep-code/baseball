#!/usr/bin/python3
import time
import globals
from utils import Image as imageUtils
from game import Game
from menu import CreateMenu
from display import Clear, ShowSplash
import tkinter as tk
from tkinter import ttk, Canvas

def PlayBall():
	globals.initialize()
	app = tk.Tk()
	app.title('Baseball')
	app.wm_attributes('-type', 'splash')
	globals.screenWidth = app.winfo_screenwidth()
	globals.screenHeight = app.winfo_screenheight()
	app.geometry(str(globals.screenWidth) + 'x' + str(globals.screenHeight) + '+0+0')    
	app['background'] = '#000000'
	canvas = Canvas(app, bg = '#000000', width = globals.screenWidth, height = globals.screenHeight)
	canvas.pack()

	
	if globals.splashDisplayed == False:
		imageUtils.emptyCache()
		showSplash = ShowSplash(canvas)
		app.update()
		splashDisplayed = True
		time.sleep(5)

	
	
	# Show Game
	if globals.gameSelected == True and globals.gameInProgress == True:
		clear = Clear(canvas)
		#showGame = Game(canvas).getCurrentPlay()

	# Show Menu
	else:
		clear = Clear(canvas)
		showMenu = CreateMenu(canvas)
		showMenu.pack(fill='both', expand=True)
		app.update()
	
	app.mainloop()


try:
	playBall = PlayBall()

except KeyboardInterrupt:
	app.destroy()
	sys.exit(1)

