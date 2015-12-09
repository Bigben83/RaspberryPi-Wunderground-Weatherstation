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

# ------------------GATHER & UPLOAD------------------------
# Loop to continously upload data (with delay)
while(True):
#	currentDate=str(datetime.utcnow())
#	currentDate=currentDate.split(" ")
#	strDate=currentDate[0] + "%" + currentDate[1]

# Try to grab a sensor reading.  Use the read_retry method which will retry up
	humidity, temperature = Adafruit_DHT.read_retry(DHT_sensor, DHT_pin)
	temp = BMP_sensor.read_temperature()
	preI = BMP_sensor.read_pressure()
	preBI = h_to_i(preI)
	F_temp = get_c_to_f(temp)
	F_temp2 = get_c_to_f(temperature)
#	pressure = BMP_sensor.read_pressure()
	pressure_sfc = get_sfc_pres()
	precip_sfc = get_precip()
	dewptf = dewpoint_f(F_temp, humidity)
	
	if humidity is not None and temperature is not None:
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	else:
		print 'Failed to get reading. Try again!'

# upload data to Wunderground
	try:
			conn = httplib.HTTPConnection("rtupdate.wunderground.com")
			path = ("/weatherstation/updateweatherstation.php?ID=" + station_id
					+ "&PASSWORD=" + urllib.quote(password)
					+ "&dateutc=" + urllib.quote(str(datetime.utcnow()))
					+ "&tempf=" + str(F_temp)       # [F outdoor temperature]
					+ "&temp2f=" + str(F_temp2)     # [F outdoor sensor 2 temperature]
					+ "&humidity=" + str(humidity)  # [% outdoor humidity 0-100%]
					+ "&baromin=" + str(preBI)      # [barometric pressure inches]
					+ "&rainin=" + str(precip_sfc)  # [rain inches over the past hour]
#					+ "&dailyrainin=" + str(data[precip_sfc])   # [rain inches so far today in local time]
					+ "&dewptf=" + str(dewptf)      # [F outdoor dewpoint F]
#					+ "&winddir=" + str(data[winddir]) # [0-360 instantaneous wind direction]
#					+ "&windspeedmph=" + str(data[windspeedmph])
#         + "&windspdmph_avg2m=" + str(data[windspdmph_avg2m])      # [mph 2 minute average wind speed mph]
#         + "&soiltempf=" + str(data[soiltempf])  # [F soil temperature]
#         + "&soilmoisture=" + str(data[soilmoisture])  # [%]
#         + "&leafwetness=" + str(data[leafwetness])    # [%]
#         + "&solarradiation=" + str(data[solarradiation])  # [W/m^2]
#         + "&UV=" + str(data[UV])  # [Index]
					+ "&softwaretype=RaspberryPi&action=updateraw&realtime=1&rtfreq=60") # [rtfreq should match FREQUENCY_SECONDS]
			print path
			conn.request("GET", path)
			res = conn.getresponse()
			#res = urllib2.urlopen(path).read()
			# checks whether there was a successful connection (HTTP code 200 and content of page contains "success")
			if (int(res.status) == 200):
				print "Successful Upload: " + res.read()
			else:
				print "Upload not successful. %i" % res.status
	except IOError as e: #in case of any kind of socket error
		print "{0} -- I/O error({1}): {2} will try again in {2} seconds".format(datetime.now(), e.errno, e.strerror)
		print e

# Wait before re-uploading data
	time.sleep(FREQUENCY_SECONDS)
