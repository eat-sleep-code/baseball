import os
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ShowSplash:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = Image.open(os.path.join(os.getcwd(), 'images/splash-screen.jpg'))
        self.splashScreenImage = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor='center', image=self.splashScreenImage)
        time.sleep(5)

        
        
        

        