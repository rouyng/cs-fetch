# python script for interactively fetching license information given a callsign
# Uses HamQTH API, see https://www.hamqth.com/developers.php
# You must have a HamQTH account as the API requires a valid username and password to start a session

import requests
import xml.etree.ElementTree as ET
import sys
import configparser
from datetime import datetime
from datetime import timedelta

def getsession():
    sessionReq = requests.get('https://www.hamqth.com/xml.php?u={}&p={}'.format(username, password))
    sessionReq.raise_for_status()               # check whether HTTP request was successful
    ## need to handle exception for timeouts/network errors etc here, add retry loop
    root = ET.fromstring(sessionReq.content)    # get XML tree from HTTPS request results
    sessionID = root[0][0].text
    if sessionID == 'Wrong user name or password':
        print("Wrong user name or password!")
        sys.exit(1)         # exit if credentials are wrong. eventually will implement input prompts for new credentials
    else:
        expireTime = datetime.now() + timedelta(hours = 1)
        config.set('Session', 'SID', str(sessionID))
        config.set('Session', 'EXP', str(expireTime))
        config.write(open('cf.conf','w'))
        print('Connected to HamQTH.com as {}\nSession ID: {}\nExpires {}'.format(username, sessionID, expireTime.strftime('%H:%M:%S')))  # session is valid for one hour, print expiration time when new session is requested
        return sessionID

def inputcallsign():
    callsign = ''
    while True:
        callsign = input('Enter Callsign to Lookup:')
        if len(callsign) < 3 or len(callsign) > 7:
            print('{} does not appear to be a valid callsign format, please try again.'.format(callsign))
            callsign = ''
            continue
        else:
            return callsign

def fetchcallsigndata():
    callsignreq = requests.get('https://www.hamqth.com/xml.php?id={}&callsign={}&prg=callsignfetch'.format(sid, csign))
    callsignreq.raise_for_status()      #check whether HTTP request was successful
    csroot = ET.fromstring(callsignreq.content)
    qtherror = csroot.find('*/{https://www.hamqth.com}error')
    if qtherror != None:
        print('HamQTH Error: {}'.format(qtherror.text))
        return False
    else:
        csdict = {}
        for child in csroot[0]:
            tag = child.tag
            csdict[tag.split('}')[1]] = child.text
        try:
            print('Name: {}'.format(csdict['adr_name']))
            print('QTH: {}'.format(csdict['qth']))
            print('Country: {}'.format(csdict['country']))
            print('Grid: {}'.format(csdict['grid']))
            print('Email: {}'.format(csdict['email']))
        except KeyError as e:
            print('{} is not found!'.format(e))
        again = ''
        while again not in ['y', 'n']:
            again = input("Do you want to lookup another callsign? (y/n) ").lower()
            if again == 'y':
                return False
                break
            elif again == 'n':
                return True
                break
            else:
                continue

config = configparser.ConfigParser()
config.read('cf.conf')                              # read configuration file cf.conf
username = config.get('Credentials', 'User')        # The user's callsign
password = config.get('Credentials', 'Password')    # HamQTH password
expireTime = config.get('Session', 'EXP')           # Session expiration date/time

if datetime.now() >= datetime.strptime(expireTime.split('.')[0], '%Y-%m-%d %H:%M:%S'):
    sid = getsession()
else:
    sid = config.get('Session', 'SID')              # Existing session ID
    print('Existing session found\nSession ID: {}'.format(sid))

while True:
    csign = inputcallsign()
    if not fetchcallsigndata():
        continue
    else:
        break

