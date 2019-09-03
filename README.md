# Callsign Info Fetcher
A simple Python script to lookup amateur radio license information via the HamQTH.com API. By Ross, KJ7GES

## Overview
This script interactively takes callsigns as an input, looks them up in the HamQTH.com database, and returns several info fields if the callsign exists in the database. Designed for simple, quick operation when you don't want to use a logging program or deal with a mouse-driven web UI and just want basic information about the callsign. 

Features include:
- reading credentials from a configuration file
- storing and recalling an active session if the script is stopped
- HTTP request error handling
- simple validation of input based on length

You can read more about the HamQTH API here: https://www.hamqth.com/developers.php

This is a basic Python script primarily written as a practice exercise, so any suggestions or constructive critique is welcome.

## Use
Tested with Python 3.7.0

Edit cf.conf with your HamQTH.com credentials before running. You must have a HamQTH account for the script to work! The fields under the "Session" section should be left blank, these are used by the script to store session information.

```
pip3 install -r requirements.txt
python -m cf.py
```

## Important Files
- `cf.py`: This is the script
- `cf.conf`: This is the configuration file for the script, enter your HamQTH.com credentials here before use.
- `requirements.txt`: python requirements file

## TODO
- Currently the choice of specific fields returned from HamQTH is hardcoded. Planning on making this configurable by modifying lines in the config file.
- Need to automatically request a new session if the current session expires while the script is running.
- More sophisticated input validation based on all possible valid callsign formats

## License
This project is released under the terms of the GNU GPL v3.0. See LICENSE file for details.
