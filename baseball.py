#!/usr/bin/python3
import time
from game import Game
from menu import Menu
from display import Clear, ShowSplash
import tkinter as tk
from tkinter import ttk, Canvas
from PIL import Image, ImageTk


app = tk.Tk()
app.title('Baseball')
app.wm_attributes('-type', 'splash')
app.geometry(str(app.winfo_screenwidth()) + 'x' + str(app.winfo_screenheight()) + '+0+0')    
app['background'] = '#000000'
canvas = Canvas(app, width = app.winfo_screenwidth(), height = app.winfo_screenheight())
canvas.pack()

# Show Splash
showSplash = ShowSplash(canvas)
app.update()
time.sleep(5)

# Show Menu
clear = Clear(canvas)
showMenu = Menu(canvas).createMenu()
app.update()





time.sleep(10)



