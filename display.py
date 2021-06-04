import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


currentDirectory = os.getcwd() + '/baseball/'

class Display:

    def clear(canvas):
        canvas.delete("all")
    
    def showSplash(canvas):
        global currentDirectory
        canvas.delete("all")
        image = Image.open(os.path.join(currentDirectory, 'images/splash-screen.jpg'))
        splashScreenImage = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=splashScreenImage)

		# exitButton = ttk.Button(root, compound=tk.CENTER, image=exitImage, command=lambda: Buttons.handler(buttonDictionary, 'exit'))
		# exitButton['style'] = 'default.TButton'
		# exitButton.place(x=borderLeft,y=0,width=buttonWidth,height=buttonHeight)


        