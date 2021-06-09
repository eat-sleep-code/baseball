import globals
import os
import pygame
import time


class Clear:
    def __init__(self):
        globals.displaySurface.fill((0, 0, 0))
        pygame.display.update()

class ShowSplash:
    def __init__(self):
        pygame.display.set_caption(globals.title)
        splashImagePath = os.path.join(globals.homePath, 'images/splash-screen.jpg')
        splashImage = pygame.image.load(splashImagePath)
        globals.displaySurface.blit(splashImage, (0, 0))
        pygame.display.update()
