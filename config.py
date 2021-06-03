import json
import os
import subprocess

configFile = os.getcwd() + '/config.json'
favoriteTeam = ''
deviceType = 'pi'
scheduleUrl = 'https://statsapi.mlb.com/api/v1/schedule/games?sportId=1'
gameDataUrl = 'http://statsapi.mlb.com/api/v1.1/game/[GAMEID]/feed/live'

class Config:

	def read():
		global configFile
		global favoriteTeam
		global deviceType 
		global scheduleUrl 
		global gameDataUrl
		try:	
			with open(configFile) as configData:
				configList = json.load(configData)
				for configItem in configList: 
					favoriteTeam = configItem['favoriteTeam']
					deviceType = config['deviceType']
					scheduleUrl = configItem['scheduleUrl']
					gameDataUrl = configItem['gameDataUrl'] 
		except:
			Config.write(favoriteTeam, deviceType, scheduleUrl, gameDataUrl)
			pass
		return(favoriteTeam, deviceType, scheduleUrl, gameDataUrl)


	def write(favoriteTeam, deviceType, scheduleUrl, gameDataUrl): 
		global configFile
		try:
			
			configList = []
			configList.append({
				'favoriteTeam': str(favoriteTeam),
				'deviceType': str(deviceType),
				'scheduleUrl': str(scheduleUrl),
				'gameDataUrl': str(gameDataUrl)
			})

			with open(configFile, 'w') as configData:
				json.dump(configList, configData, indent=4)
			return True
		except Exception as ex:
			print(str(ex))
			return False