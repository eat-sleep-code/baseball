import base64
import cairosvg
import io
import time
import urllib
from datetime import datetime, timedelta

now = datetime.now() 

class Date:

    def UTCtoLocal(UTCdate):
        timeObject = datetime.strptime(UTCdate, '%Y-%m-%dT%H:%M:%SZ')
        timezoneOffset = -time.timezone
        adjustedDate = timeObject + timedelta(seconds=timezoneOffset)
        return adjustedDate

    

class Image:

    def WebImageToBase64(imageUrl):
        request = urllib.request.Request(imageUrl, headers={'User-Agent': "Baseball Pi"})
        connection = urllib.request.urlopen(request)
        imageBytes = connection.read()
        imageBase64 = base64.encodestring(imageBytes)
        return imageBase64

    def SVGtoPNG(imageUrl):
        request = urllib.request.Request(imageUrl, headers={'User-Agent': "Baseball Pi"})
        connection = urllib.request.urlopen(request)
        imageBytes = connection.read().decode('utf-8')
        pngData = cairosvg.svg2png(bytestring=imageBytes, unsafe=True)
        print(pngData)
        pngBytes = io.BytesIO(pngData)