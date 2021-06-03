import time
from datetime import datetime, timedelta

now = datetime.now() 

class Date:

    def UTCtoLocal(UTCdate):
        timeObject = datetime.strptime(UTCdate, '%Y-%m-%dT%H:%M:%SZ')
        timezoneOffset = -time.timezone
        adjustedDate = timeObject + timedelta(seconds=timezoneOffset)
        return adjustedDate

    
