# Cs-Fetch
A simple Python-based program to lookup amateur radio license information via the HamQTH.com API. Includes GUI and 
interactive command-line interfaces.

By Ross, KJ7GES

## Overview
Cs-Fetch (or Callsign-Fetch) is intended to be a simple, fast and flexible way to look up information about
amateur (ham) radio callsigns. It is not intended to replace logging programs or web databases, just as an aid to
radio operation and monitoring. Currently supports pulling information from the HamQTH.com database, with plans to
allow selectable use of FCC and QRZ.com databases.

Features include:
- Command-line and GUI-based interface
- User-configurable results
- API session memory and auto-renewal
- Basic validation of callsign input
- Cross-platform with QT-based GUI 

You can read more about the HamQTH API here: https://www.hamqth.com/developers.php
<a href="https://www.hamqth.com">
    <img src="https://www.hamqth.com/images/hamqth_460x60.png" border="1" height="60" width="460" alt="HamQTH.com - Free hamradio callbook">
</a> 

## Use
Tested with Python 3.7.0

Before running, add your HamQTH.com credentials to the `[Credentials]` section in `cf.conf`. 
You must have your own HamQTH account for the script to work!

To run, from the installation directory:
```
pip3 install -r requirements.txt
python -m cf
```

Substitute cf-gui for cf if you want to run the GUI version (currently under development).

By default the script will print all fields returned by HamQTH that are not empty. This can be configured by commenting
out lines under `[Fields]` in `cf.conf`. The order in which fields are printed can also be changed by reordering this section.

## Important Files
- `cf.py`: This is the script (command line version)
- `cf-gui.py` Script (GUI version)
- `cf.conf`: This is the configuration file for the script, enter your HamQTH.com credentials here before use.
- `requirements.txt`: python requirements file

## TODO
- complete GUI version, currently in progress
- windows/linux/mac packaging
- support fetching from FCC and QRZ databases
- offline mode, lookup of location based on callsign prefix

## License
This project is released under the terms of the GNU GPL v3.0. See LICENSE file for details.

