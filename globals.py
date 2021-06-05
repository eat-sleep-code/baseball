import os

def initialize():
    global splashDisplayed
    splashDisplayed = False
    
    global gameSelected
    gameSelected = False

    global gameInProgress
    gameInProgress = False

    global imageCache
    imageCache = os.getcwd() + '/images/cache/'