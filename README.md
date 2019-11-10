# Callsign Info Fetcher
A simple Python script to lookup amateur radio license information via the HamQTH.com API.

By Ross, KJ7GES

## Overview
This script interactively takes amateur (ham) radio callsigns as an input, looks them up in the HamQTH.com database, and returns several info fields if the callsign exists in the database. Designed for simple, quick operation when you don't want to use a logging program or deal with a mouse-driven web UI and just want basic information about the callsign. 

Features include:
- reading credentials from a configuration file
- can configure which fields are returned and their order, from configuration file
- storing and recalling an active session if the script is stopped
- HTTP request error handling
- simple validation of input based on length

You can read more about the HamQTH API here: https://www.hamqth.com/developers.php

This is a basic Python script primarily written as a practice exercise, suggestions and constructive critique are welcome.

## Use
Tested with Python 3.7.0

Before running, add your HamQTH.com credentials to the `[Credentials]` section in `cf.conf`. 
You must have your own HamQTH account for the script to work!

To run, from the installation directory:
```
pip3 install -r requirements.txt
python -m cf
```

By default the script will print all fields returned by HamQTH that are not empty. This can be configured by commenting
out lines under `[Fields]` in `cf.conf`. The order in which fields are printed can also be changed by reordering this section.

## Important Files
- `cf.py`: This is the script
- `cf.conf`: This is the configuration file for the script, enter your HamQTH.com credentials here before use.
- `requirements.txt`: python requirements file

## TODO
- Need to automatically request a new session if the current session expires while the script is running.
- PyQt5 GUI (in progress, see [pyqt-gui branch](https://github.com/rouyng/callsign-fetch/tree/pyqt-gui))

## License
This project is released under the terms of the GNU GPL v3.0. See LICENSE file for details.
