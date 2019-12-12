# cs-fetch
A simple program to lookup amateur radio call sign information via the HamQTH.com API. Includes GUI and 
interactive command-line interfaces.

By Ross, KJ7GES

## Overview
cs-fetch (or callsign-fetch) is intended to be a simple, fast and flexible way to look up information about
amateur (ham) radio call signs. It is not intended to replace logging programs or web databases, just as an aid to
radio operation and monitoring. Currently supports fetching information from the HamQTH.com database, with plans to
allow selectable use of FCC and QRZ.com databases. cs-fetch is written in Python and uses PyQt5 for the GUI interface. 
Bug/issue reports and code contributions are welcome.

Features include:
- Interactive command line and GUI interfaces
- User-configurable results
- API session memory and auto-renewal
- Basic validation of callsign input
- Cross-platform with QT-based GUI 

You can read more about the HamQTH API here: https://www.hamqth.com/developers.php
<a href="https://www.hamqth.com">
    <img src="https://www.hamqth.com/images/hamqth_460x60.png" border="1" height="60" width="460" alt="HamQTH.com - Free hamradio callbook">
</a> 

## Installation
cs-fetch was written and tested with Python 3.7.0, so you should have this version or a newer installed.
It may work with earlier versions of Python, but I have not tested this.

Download/clone the repository into your directory of choice. To install all required python packages, run this 
command in the installation directory:
```
pip3 install -r requirements.txt
```

Before running, add your HamQTH.com credentials to the `[Credentials]` section in `cf.conf`. 
You can create a HamQTH account here.

By default the program will print all fields returned by HamQTH that are not empty. This can be configured by
setting any undesired fields to `field_name = no` under`[Fields to print]` in `cf.conf`. 
The order in which fields are printed can also be changed by reordering this section.

## Usage
For the GUI version, run from the installation directory:
```
python cfgui.py
```

For the command line version, run from the installation directory:
```
python cf.py
```

## Important Files
- `cf.py`: cs-fetch command line version
- `cfgui.py` cs-fetch GUI version
- `cf.conf`: This is the configuration file for the script, enter your HamQTH.com credentials here before use.
- `/gui`: Contains required files for the PyQt5 GUI
- `requirements.txt`: python requirements file

## TODO
- Windows/linux/mac executable packaging
- Support fetching from FCC and QRZ databases
- Offline mode, lookup of location based on callsign prefix
- Dark mode GUI skin!

## License
This project is released under the terms of the GNU GPL v3.0. See LICENSE file for details.

