import json
import os
import subprocess

configFile = os.getcwd() + '/config.json'
favoriteTeam = ''
deviceType = 'pi'
apiUrl = 'https://statsapi.mlb.com'
scheduleUrl = 'https://statsapi.mlb.com/api/v1/schedule/games?sportId=1'
logoUrl = 'https://www.mlbstatic.com/team-logos/[TEAMID].svg'

class Config:

	def read():
		global configFile
		global favoriteTeam
		global deviceType 
		global apiUrl
		global scheduleUrl 
		global logoUrl
		
		try:	
			with open(configFile) as configData:
				configList = json.load(configData)
				for configItem in configList: 
					favoriteTeam = configItem['favoriteTeam']
					deviceType = config['deviceType']
					apiUrl = configItem['apiUrl']
					scheduleUrl = configItem['scheduleUrl']
					logoUrl = configItem['logoUrl']
		except:
			Config.write(favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl)
			pass
		return(favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl)


	def write(favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl): 
		global configFile
		try:
			
			configList = []
			configList.append({
				'favoriteTeam': str(favoriteTeam),
				'deviceType': str(deviceType),
				'apiUrl': str(apiUrl),
				'scheduleUrl': str(scheduleUrl),
				'logoUrl': str(logoUrl)
			})

			with open(configFile, 'w') as configData:
				json.dump(configList, configData, indent=4)
			return True
		except Exception as ex:
			print(str(ex))
			return False


		