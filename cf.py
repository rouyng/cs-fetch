# python script for interactively fetching license information given a callsign
# Uses HamQTH API, see https://www.hamqth.com/developers.php
# You must have a HamQTH account as the API requires a valid username and password to start a session

import configparser
import json
import string
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import timedelta
from os.path import isfile

import requests


# BEGIN FetchSession Class
class FetchSession():
    """
    Class for requesting callsign data from the HamQTH API.

    Credentials and fields to return are all taken from the configuration file (cf.conf).
    Additional functions to support requesting data from FCC ULS and QRZ.com will eventually be added to this class.
    """
    def __init__(self, configuration_file, data_source='hamqth'):
        self._configfile = configuration_file  # configuration file, should be cf.conf
        self._config = configparser.ConfigParser(inline_comment_prefixes='#')
        self.username = ''  # API username
        self.password = ''  # API password
        self.session_error = False
        self.field_list = []  # list of fields to print based on user configuration
        self.session_id = ''  # session ID supplied by remote API
        self.source = data_source  # placeholder for switching to QRZ and FCC dbs, as well as original hamqth
        # field_labels dict contains the human-friendly labels for each field the API may return
        self.field_labels = {'callsign': 'Callsign',
                             'nick': 'Nickname',
                             'qth': 'QTH',
                             'country': 'Country',
                             'adif': 'ADIF ID',
                             'itu': 'ITU',
                             'cq': 'CQ (WAZ) zone',
                             'grid': 'Grid Square',
                             'adr_name': 'Name (from address)',
                             'adr_street1': 'Address 1',
                             'adr_street2': 'Address 2',
                             'adr_street3': 'Address 3',
                             'adr_city': 'City',
                             'adr_zip': 'Zip/postal code',
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
        self.session_initialize()
        self._get_fields_to_print()

    def session_initialize(self):
        """Reads credentials from config file and establishes a new/existing session"""
        self.session_error = False
        self.session_id = None
        if self.username == '' or self.password == '':
            # if username/password are blank, read config file
            # otherwise, if they are not we can expect the new username/password have been set by write_config()
            if isfile(self._configfile):
                self._config.read(self._configfile)  # read configuration file cf.conf
                self.username = self._config.get('Credentials', 'User')  # The user's callsign is read from cf.conf
                self.password = self._config.get('Credentials', 'Password')  # User's password is read from cf.conf
            else:
                raise FileNotFoundError(f'The specified configuration file {self._configfile} was not found')
        try:
            with open('session.json') as f:
                existing_session = json.load(f)
                if existing_session['SID']:
                    expire_time = existing_session['EXP']  # Existing session expiration date/time read from session.json
                    sid = existing_session['SID']  # Existing session ID read from session.json
                    if datetime.now() >= datetime.strptime(expire_time.split('.')[0], '%Y-%m-%d %H:%M:%S'):
                        self.get_session_hamqth(self.username, self.password)
                    else:
                        print('Existing session found\nSession ID: {}'.format(sid))
                        self.session_id = sid
                else:
                    self.get_session_hamqth(self.username, self.password)
        except FileNotFoundError:
            self.get_session_hamqth(self.username, self.password)

    def get_session_hamqth(self, username, password):
        """Gets a new session ID from the HamQTH API, with error handling if credentials wrong or connection broken"""
        print(f'Starting new {self.source} session as {self.username}...')
        try:
            session_req = requests.get(f'https://www.hamqth.com/xml.php?u={username}&p={password}')
            session_req.raise_for_status()  # check whether HTTP request was successful
            root = ET.fromstring(session_req.content)  # get XML tree from HTTPS request results
            session_id = root[0][0].text
            if session_id == 'Wrong user name or password':
                raise ConnectionError("Wrong user name or password! Please enter valid HamQTH credentials in cf.conf")
            else:
                expire_time = datetime.now() + timedelta(hours=1)
                session_dict = {'SID': str(session_id), 'EXP': str(expire_time)}
                with open('session.json', 'w') as e:  # store session_dict in JSON file
                    json.dump(session_dict, e)
                exp_formatted = expire_time.strftime('%H:%M:%S')
                print(
                    f'Connected to HamQTH.com as {username}\nSession ID: {session_id}\nExpires {exp_formatted}')
                self.session_id = session_id
        except (requests.exceptions.ConnectionError, ConnectionError) as se:
            self.session_error = se

    def get_session_qrz(self, username, password):
        """Gets a new session ID from the QRZ.com API, with error handling if credentials wrong or connection broken"""
        print(f'Starting new QRZ session as {username}...')
        try:
            session_req = requests.get(
                f'http://xmldata.qrz.com/xml/current/?username={username};password={password};agent=csf0.6')
            session_req.raise_for_status()  # check whether HTTP request was successful
            root = ET.fromstring(session_req.content)  # get XML tree from HTTPS request results
            session_id = root[0][0].text
            if session_id == 'Username/password incorrect ':
                raise ConnectionError("Wrong user name or password! Please enter valid QRZ.com credentials in cf.conf")
            else:
                session_dict = {'SID': str(session_id), 'EXP': None, 'SOURCE': 'QRZ'}
                with open('session.json', 'w') as e:  # store session_dict in JSON file
                    json.dump(session_dict, e)
                print(
                    f'Connected to QRZ.com as {username}\nSession ID: {session_id}')
            self.session_id = session_id
        except (requests.exceptions.ConnectionError, ConnectionError) as se:
            session_error = se
            print(session_error)

    def _get_fields_to_print(self):
        """Set self.field_list variable with fields that should be printed from configuration file"""
        self.field_list = []
        for f in self._config.options('Fields to print'):
            if self._config.getboolean('Fields to print', f):
                self.field_list.append(f)

    def write_config(self, new_fields, new_username, new_password, new_source, dark_mode):
        """write changed configuration to the configfile and re-initialize session"""
        for f in self._config.options('Fields to print'):
            if f in new_fields:
                self._config.set('Fields to print', f, 'yes')
            else:
                self._config.set('Fields to print', f, 'no')
        if (new_username, new_password, new_source) != (self.username, self.password, self.source):
            self._config.set('Credentials', 'user', new_username)
            self._config.set('Credentials', 'password', new_password)
            self._config.set('Database', 'source', new_source)
            self.username = new_username
            self.password = new_password
            self.source = new_source
            with open('session.json', 'w') as e:  # store session_dict in JSON file
                json.dump({'SID': None, 'EXP': None}, e)
        if dark_mode:
            self._config.set('Theme', 'darkmode', 'yes')
        else:
            self._config.set('Theme', 'darkmode', 'no')
        with open(self._configfile, 'w') as file:  # write the configuration file
            self._config.write(file)
        self.session_initialize()
        self._get_fields_to_print()

# END FetchSession Class

# BEGIN STATIC FUNCTION DEFINITIONS


def validate_callsign(cs):
    """
    This function accepts input of callsign to be looked up and checks it against callsign conventions.

    Returns False if it appears to be valid, otherwise it returns an error message.
    """
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
            cs_err = f'{cs} does not appear to be a valid callsign format (callsigns contain both letters and digits)'
        else:
            return False
    return cs_err


def fetch_callsign_data(session_id, callsign):
    """
    This function requests information from the HamQTH API given a valid session ID and callsign.

    If the API returns an error (including if the callsign is not found), this function returns the error message str
    If the callsign's info is found on HamQTH, the function returns info in a dict
    """
    try:
        callsignreq = requests.get(f'https://www.hamqth.com/xml.php?id={session_id}&callsign={callsign}&prg=cs-fetch')
        callsignreq.raise_for_status()  # check whether HTTP request was successful
        csroot = ET.fromstring(callsignreq.content)
        if 'error' in csroot[0][0].tag:
            qtherror = csroot[0][0].text
            return qtherror
        else:
            csdict = {}
            for child in csroot[0]:
                tag = child.tag
                csdict[tag.split('}')[1]] = child.text
            return csdict
    except requests.exceptions.ConnectionError as fe:
        return 'Connection error, please check your internet connection'


def print_callsign_info(callsign_dictionary, labels, print_these_fields=('adr_name')):
    """This function prints selected fields from the dict returned by fetchcallsign, along with human-friendly labels"""
    for key in print_these_fields:
        if key in labels.keys() & callsign_dictionary.keys():
            print('{}: {}'.format(labels[key], callsign_dictionary[key]))


# END FUNCTION DEFINITIONS


# MAIN SEQUENCE BEGIN

if __name__ == "__main__":
    configfile = 'cf.conf'
    session = FetchSession(configfile)
    if session.session_error:
        print(f'Unable to connect to server, please check your internet connection')
        print(session.session_error)
        sys.exit(1)
    callsign = ''
    while True:
        while True:
            user_input = input('Enter Callsign to Lookup: ')
            if not validate_callsign(user_input):
                callsign = user_input
                break
            else:
                print(validate_callsign(user_input))
                continue
        callsign_result = fetch_callsign_data(session.session_id, callsign)  # request info from API and return as dict
        if callsign_result.__class__ != dict:
            print(f'Error: {callsign_result}')  # Errors returned by API should be a string, real results are a dict
            if 'Session does not exist or expired' in callsign_result:
                # re-initialize session if expired
                print('Attempting to start a new session...')
                session.session_initialize()
        else:
            print_callsign_info(callsign_result, session.field_labels, session.field_list)  # Print results from API request
        # Ask if we want to look up another callsign
        again = input("Do you want to lookup another callsign? (y/n) ").lower()
        if again == 'y':
            continue
        elif again == 'n':
            print('Exit!')
            break
