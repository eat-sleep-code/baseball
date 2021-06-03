import datetime
import json
import sys
import requests
from config import Config
from menu import Menu


global favoriteTeam
global deviceType 
global scheduleUrl 
global gameDataUrl

favoriteTeam, deviceType, scheduleUrl, gameDataUrl = Config.read()

Menu.createMenu(scheduleUrl, favoriteTeam)

