import base64
import cairosvg
import io
import globals
import os
import time
import urllib
from datetime import datetime, timedelta

now = datetime.now() 

class Date:

	def utcToLocal(UTCdate):
		timeObject = datetime.strptime(UTCdate, '%Y-%m-%dT%H:%M:%SZ')
		timezoneOffset = -time.timezone
		adjustedDate = timeObject + timedelta(seconds=timezoneOffset)
		return adjustedDate



class Image:

	def emptyCache():
		for file in os.listdir(globals.imageCache): 
			os.remove(globals.imageCache + file)


	def webImage(imageUrl):
		inputFile = globals.imageCache + imageUrl.split('/')[-1]
		outputFile = inputFile.replace('.svg', '.png')
		if os.path.exists(inputFile) == False:
			opener = urllib.request.build_opener()
			opener.addheaders=[('User-Agent','Baseball Pi')]
			urllib.request.install_opener(opener)
			urllib.request.urlretrieve(imageUrl, inputFile)
		if inputFile.endswith('.svg') and os.path.exists(outputFile) == False:
			outputFile = Image.svgToPNG(inputFile)
		return outputFile


	
	def svgToPNG(inputFile):
		outputFile = inputFile.replace('.svg', '.png')
		cairosvg.svg2png(url=inputFile, write_to=outputFile, output_width=256, output_height=256)
		return outputFile