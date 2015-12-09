# This datalogger script is responsible for collecting meteorological
# information from the following sensors

# Last updated: 2015-12-09
# Created by Benjamin Harris

import sys
import os
import glob
import time
import httplib
import urllib, urllib2
from datetime import datetime

# ------------------IMPORT SENSOR DATA----------------------
import sensors
import conversion

# ------------------CONFIGURATION--------------------------
# Wunderground personal weather station ID/password
station_id = "STATIONID"
password = "PASSWORD"

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 60
