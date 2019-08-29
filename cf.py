# python script for interactively fetching license information given a callsign
# Uses HamQTH API, see https://www.hamqth.com/developers.php
# You must have a HamQTH account as the API requires a valid username and password to start a session

import requests
import xml.etree.ElementTree as ET
import sys
from datetime import datetime
from datetime import timedelta

username = 'KJ7GES'         # should be the user's callsign
password = ']F_l2;stY![r'   # HamQTH password

def getSession():
    sessionReq = requests.get('https://www.hamqth.com/xml.php?u={}&p={}'.format(username, password))
    sessionReq.raise_for_status()               #check whether HTTP request succeeded
    root = ET.fromstring(sessionReq.content)    #get XML tree from HTTPS request results
    sessionID = root[0][0].text
    elif sessionID == 'Wrong user name or password':
        print("Wrong user name or password!")
        sys.exit(1)         # for now, just exit if credentials are wrong. eventually will implement input prompts for new credentials
    else:
        expireTime = datetime.now() + timedelta(hours = 1)
        print('Session ID: {}\nExpires {}'.format(sessionID, expireTime.strftime('%H:%M:%S'))) # session is valid for one hour, print expiration time when new session is requested

def getCallsign():
    callsign = ''
    input('Enter Callsign to lookup:', callsign)
    # insert some validation

getSession()
getCallsign()