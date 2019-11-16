# python script for interactively fetching license information given a callsign
# Uses HamQTH API, see https://www.hamqth.com/developers.php
# You must have a HamQTH account as the API requires a valid username and password to start a session

import configparser
import sys
import json
import requests
import string
import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import timedelta


## BEGIN FUNCTION DEFINITIONS

# This function requests a new session from the HamQTH API
def getsession(username, password):
    sessionReq = requests.get(f'https://www.hamqth.com/xml.php?u={username}&p={password}')
    sessionReq.raise_for_status()  # check whether HTTP request was successful
    ## need to handle exception for timeouts/network errors etc here, add retry loop
    root = ET.fromstring(sessionReq.content)  # get XML tree from HTTPS request results
    sessionID = root[0][0].text
    if sessionID == 'Wrong user name or password':
        print("Wrong user name or password! Please enter valid HamQTH.com credentials in cf.conf")
        sys.exit(1)  # exit if credentials are wrong
    else:
        expireTime = datetime.now() + timedelta(hours=1)
        session_dict = {'SID': str(sessionID), 'EXP': str(expireTime)}
        with open('session.json', 'w') as e:  # store session_dict in JSON file
            json.dump(session_dict, e)
        exp_formatted = expireTime.strftime('%H:%M:%S')
        print(
            f'Connected to HamQTH.com as {username}\nSession ID: {sessionID}\nExpires {exp_formatted}')  # session is valid for one hour, print expiration time when new session is requested
        return sessionID


def validatecallsing(cs):
    # This function accepts input of callsign to be looked up and checks it against callsign conventions
    # returns True if it appears to be valid, otherwise it prints an error message and returns False
    cs_err = ''  # this string stores any callsign validation error
    valid_chars = string.digits + string.ascii_letters  # callsigns should only contain letters and digits
    while cs_err == '':
        if any(c not in valid_chars for c in cs):  # check if any invalid characters are present in the input
            cs_err = f'{cs} does not appear to be a valid callsign format (contains invalid character)'
        elif len(cs) < 3:
            cs_err = f'{cs} does not appear to be a valid callsign format (too short)'
        elif len(cs) > 7:
            cs_err = f'{cs} does not appear to be a valid callsign format (too long)'
        elif not any(d in cs for d in string.digits) or not any(l in cs for l in string.ascii_letters):
            cs_err = f'{cs} does not appear to be a valid callsign format (callsigns must contain both letters and digits)'
        else:
            return True
    print(cs_err)
    return False

# This function requests information from the HamQTH API given a valid session ID and callsign, returns info in a dict
def fetchcallsigndata(session_id, callsign):
    callsignreq = requests.get(
        'https://www.hamqth.com/xml.php?id={}&callsign={}&prg=callsignfetch'.format(session_id, callsign))
    callsignreq.raise_for_status()  # check whether HTTP request was successful
    csroot = ET.fromstring(callsignreq.content)
    qtherror = csroot.find('*/{https://www.hamqth.com}error')
    if qtherror:
        print('HamQTH Error: {}'.format(qtherror.text))
        return False
    else:
        csdict = {}
        for child in csroot[0]:
            tag = child.tag
            csdict[tag.split('}')[1]] = child.text
    return csdict


# This function prints selected fields from the dict returned by fetchcallsign data, along with human-friendly labels
def print_callsign_info(callsign_dictionary, print_these_fields=['adr_name']):
    # field_labels dict contains the human-friendly labels for each field the API may return
    field_labels = {'callsign': 'Callsign',
                    'nick': 'Nickname',
                    'qth': 'QTH',
                    'country': 'Country',
                    'adif': 'ADIF ID',
                    'itu': 'ITU',
                    'CQ': 'CQ (WAZ) zone',
                    'grid': 'Grid Square',
                    'adr_name': 'Name (from address)',
                    'adr_street1': 'Address 1',
                    'adr_street2': 'Address 2',
                    'adr_street3': 'Address 3',
                    'adr_city': 'City',
                    'adr_zip': 'Zip code',
                    'adr_country': 'Country (from address)',
                    'adr_adif': 'ADIF (from address)',
                    'district': 'District',
                    'us_state': 'State (USA)',
                    'us_county': 'County (USA)',
                    'oblast': 'Oblast (RUS)',
                    'dok': 'DOK',
                    'iota': 'IOTA #',
                    'qsl_via': 'QSL Info',
                    'lotw': 'Uses LOTW?',
                    'eqsl': 'Uses EQSL?',
                    'qsl': 'Accept QSL via bureau?',
                    'qsldirect': 'Accept direct QSL card?',
                    'email': 'Email address',
                    'jabber': 'Jabber',
                    'icq': 'ICQ',
                    'msn': 'MSN',
                    'skype': 'Skype',
                    'birth_year': 'Year of birth',
                    'lic_year': 'Licensed since',
                    'picture': "URL to user's photo",
                    'latitude': 'Latitude',
                    'longitude': 'Longitude',
                    'continent': 'Continent',
                    'utc_offset': 'Offset to UTC time',
                    'facebook': 'Facebook URL',
                    'twitter': 'Twitter URL',
                    'gplus': 'Google Plus URL',
                    'youtube': 'YouTube URL',
                    'linkedin': 'LinkedIn URL',
                    'flicker': 'Flickr URL',
                    'vimeo': 'Vimeo URL'
                    }
    for key in print_these_fields:
        if key in field_labels.keys() & callsign_dictionary.keys():
            print('{}: {}'.format(field_labels[key], callsign_dictionary[key]))


def get_fields_to_print(configfile):
    config = configparser.ConfigParser()
    config.read(configfile)
    field_list = []
    fields = config.options('Fields')
    for f in fields:
        field_list.append(f)
    return field_list


def initialize(configfile):
    # Reads credentials from config file and establishes a new/existing session
    config = configparser.ConfigParser()
    config.read(configfile)  # read configuration file cf.conf
    username = config.get('Credentials', 'User')  # The user's callsign is read from cf.conf
    password = config.get('Credentials', 'Password')  # HamQTH password is read from cf.conf

    try:
        with open('session.json') as f:
            existing_session = json.load(f)
            expire_time = existing_session['EXP']  # Existing session expiration date/time read from session.json
            sid = existing_session['SID']  # Existing session ID read from session.json
            if datetime.now() >= datetime.strptime(expire_time.split('.')[0], '%Y-%m-%d %H:%M:%S'):
                sid = getsession(username, password)
            else:
                print('Existing session found\nSession ID: {}'.format(sid))
    except FileNotFoundError:
        sid = getsession(username, password)
    return sid

## END FUNCTION DEFINITIONS

## MAIN SEQUENCE BEGIN

if __name__ == "__main__":
    configfile = 'cf.conf'
    session = initialize(configfile)
    callsign = ''
    while True:
        while True:
            user_input = input('Enter Callsign to Lookup: ')
            if validatecallsing(user_input) == True:
                callsign = user_input
                break
            else:
                continue
        callsign_results = fetchcallsigndata(session, callsign)  # request info from API and return as dict
        print_callsign_info(callsign_results, get_fields_to_print(configfile))  # Print results from API request
        # Ask if we want to look up another callsign
        again = input("Do you want to lookup another callsign? (y/n) ").lower()
        if again == 'y':
            continue
        elif again == 'n':
            print('Exit!')
            break
