import json
import os
import subprocess

configFile = os.getcwd() + '/config.json'
favoriteTeam = ''
deviceType = 'pi'
apiUrl = 'https://statsapi.mlb.com'
scheduleUrl = 'https://statsapi.mlb.com/api/v1/schedule/games?sportId=1'
logoUrl = 'https://www.mlbstatic.com/team-logos/[TEAMID].svg',
portraitUrl = 'https://img.mlbstatic.com/mlb-photos/image/upload/w_256,q_auto:best/v1/people/[PLAYERID]/headshot/83/current'

class Config:

	def read():
		global configFile
		global favoriteTeam
		global deviceType 
		global apiUrl
		global scheduleUrl 
		global logoUrl
		global portraitUrl
		
		try:	
			with open(configFile) as configData:
				configList = json.load(configData)
				for configItem in configList: 
					favoriteTeam = configItem['favoriteTeam']
					deviceType = configItem['deviceType']
					apiUrl = configItem['apiUrl']
					scheduleUrl = configItem['scheduleUrl']
					logoUrl = configItem['logoUrl']
					portraitUrl = configItem['portraitUrl']
		except Exception as ex:
			#print(ex)
			Config.write(favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl, portraitUrl)
			pass
		return(favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl, portraitUrl)


	def write(favoriteTeam, deviceType, apiUrl, scheduleUrl, logoUrl, portraitUrl): 
		global configFile
		try:
			
			configList = []
			configList.append({
				'favoriteTeam': str(favoriteTeam),
				'deviceType': str(deviceType),
				'apiUrl': str(apiUrl),
				'scheduleUrl': str(scheduleUrl),
				'logoUrl': str(logoUrl), 
				'portraitUrl': str(portraitUrl)
			})

			with open(configFile, 'w') as configData:
				json.dump(configList, configData, indent=4)
			return True
		except Exception as ex:
			print(str(ex))
			return False


		