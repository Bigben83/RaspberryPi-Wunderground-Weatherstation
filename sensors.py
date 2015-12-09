# This datalogger script is responsible for collecting meteorological
# information from the following sensors and  creating a named pipe that
# streams that information over to the weewx driver.

# Installed sensors:
#  SHT25 (Temperature/Humidity sensor) [i2c]
#  BMP180 (Pressure) [i2c]
#  Pyronometer (homemade) [ADC]
#  Rainwise RAINEW 111 Tipping Bucket Rain Gauge [pulse]

# Last updated: 2015-12-09
# Created by Benjamin Harris

import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

# ------------------CONFIGURATION--------------------------
# Global variables
precip_pulse_cnt = 0
precip_pulse_start_time = 0
precip_pulse_stop_time = 0

# pressure
pres_mode = 1  # (0 ultralow power, 1 std, 2 high res, 3 ultrahigh res)
# bmp = BMP085(0x77, pres_mode)  # BMP085 and BMP180 are identical

# Precipitation
precip_port = 27
precip_multi = 0.0254  # Centimeters per tip

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_sensor = Adafruit_DHT.DHT11
DHT_pin = 4

# Sensor information, see BMP Adafruit driver documentation
BMP_sensor = BMP085.BMP085()

# Configure the GPIO for the RPi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)  # Rain activity (Blue)
GPIO.setup(precip_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# ------------------RAIN GUAGE--------------------------
# Function that counts rain
def callback_precip(channel):

    global precip_pulse_cnt
    precip_pulse_cnt = precip_pulse_cnt + 1  # each tip 1/100 inch
    f = open('/home/pi/bin/rain.log', 'a')
    datetime = strftime("%Y-%m-%d %H:%M:%S ", localtime())
    f.write(datetime + ' Precip detected 0.01 \n')
    f.close()

    # turn off precip until error fixed. Make sure to turn it on below as well 
    precip_pulse_cnt = 0

# Monitor GPIO for Rain
GPIO.add_event_detect(precip_port,
                      GPIO.FALLING,
                      callback=callback_precip,
                      bouncetime=300)

# Function to get data from Rain Gauge
def get_precip():
    global precip_pulse_cnt
    precip = precip_pulse_cnt * precip_multi
    precip_pulse_cnt = 0
    precip = None   
    return precip
					  
# ------------------END RAIN GUAGE--------------------------
