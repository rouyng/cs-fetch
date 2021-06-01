# cs-fetch
A simple program to lookup amateur radio call sign information via the HamQTH.com API. Includes GUI and 
interactive command-line interfaces.

**This repository is no longer actively maintained. Feel free to use and fork it, but I cannot provide support or honor feature requests**

## Overview
cs-fetch (or callsign-fetch) is intended to be a simple, fast and flexible way to look up information about
amateur (ham) radio call  as an aid to radio operation and monitoring. It is not a full featured logging 
application.
 
 Currently, cs-fetch supports fetching information from the HamQTH.com database, with plans to
allow selectable use of FCC and QRZ.com databases. 

cs-fetch is written in Python and uses PyQt5 for the GUI interface. 
Bug/issue reports and code contributions are welcome.

Features include:
- Interactive command line and GUI interfaces
- User-configurable results
- API session memory and auto-renewal
- Basic validation of callsign input
- Cross-platform with QT-based GUI
- Optional dark mode 

You can read more about the HamQTH API here: https://www.hamqth.com/developers.php
<a href="https://www.hamqth.com">
    <img src="https://www.hamqth.com/images/hamqth_460x60.png" border="1" height="60" width="460" alt="HamQTH.com - Free hamradio callbook">
</a> 

## Installation

The simplest way to run cs-fetch is to download one of the executable files pre-built for your operating system. These 
are packaged as .zip archives in the directory `executables/`. Separate executable files are provided for command line 
 and GUI versions. Before running, open `cf.conf` in your favorite text editor and add your HamQTH.com username/password
  to the `[Credentials]` section. Then you can run cs-fetch by executing `cf` (command line version) or `cfgui` 
  (GUI version).
 
 Currently executables are provided for Windows 10 (may work on earlier Windows versions, but has not been tested). 
 Ubuntu, Raspbian and Mac packages coming soon.


### Running from source
If you want to download the python source files and run the application that way, follow these instructions.

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
- Ubuntu/Raspbian/Mac executable packaging
- Support fetching from FCC and QRZ databases
- Offline mode, lookup of location based on callsign prefix

## License
This project is released under the terms of the GNU GPL v3.0. See LICENSE file for details.

