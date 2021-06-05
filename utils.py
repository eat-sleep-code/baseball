import time
import base64
from datetime import datetime, timedelta
import urllib

now = datetime.now() 

class Date:

    def UTCtoLocal(UTCdate):
        timeObject = datetime.strptime(UTCdate, '%Y-%m-%dT%H:%M:%SZ')
        timezoneOffset = -time.timezone
        adjustedDate = timeObject + timedelta(seconds=timezoneOffset)
        return adjustedDate

    

class Image:

    def WebImageToBase64(url):
        request = urllib.request.Request(url, headers={'User-Agent': "Baseball Pi"})
        connection = urllib.request.urlopen(request)
        imageBytes = connection.read()
        imageBase64 = base64.encodestring(imageBytes)
        return imageBase64