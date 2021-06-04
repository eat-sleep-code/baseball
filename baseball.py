#!/usr/bin/python3
from game import Game
from menu import Menu
from display import ShowSplash
import tkinter as tk
from tkinter import ttk, Canvas
from PIL import Image, ImageTk



root = tk.Tk()
root.title('Baseball')
root.wm_attributes('-type', 'splash')
root.geometry(str(root.winfo_screenwidth()) + 'x' + str(root.winfo_screenheight()) + '+0+0')	
root['background'] = '#000000'
canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()

ShowSplash(canvas)
#Menu.createMenu()
#Game.getCurrentPlay()


root.mainloop()