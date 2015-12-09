<h2>Raspberry_Pi Wunderground Weather Station</h2>

I have finally got around to updating my code to reflect the changes in Adafruits updated Sensor Code.
I havent quite finished adding the Rain Guage Option yet but will do that in the next day or so.

The various results that can be uploaded to wunderground are shown on this link
http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol

<b>The sensors that I am using are as follows</b></br>
* Pressure & Temperature = BMP180</br>
* Temperature & Humitity = DHT11</br>
* You could substitute the above for one device = Adafruit 10-DOF IMU Breakout - L3GD20H + LSM303 + BMP180</br>
* Rain Guage = Analogue Switching Tiping Guage</br>
* Soil Temp = 1Wire Device</br>
* Leaf Wetness = Sourced from Ebay #unknown quality yet :-)</br>

<b>I intend to add the following sensors</b></br>
* UV Sensor = Adafruit SI1145</br>
* Soil Moisture = Adafruit SLHT5 or Similar</br>
* Anemometer = Some analogue voltage</br>

<b>Installation Instructions</b></br>

Firstly Update</br>
```sudo apt-get update && apt-get upgrade -y```</br>
```sudo apt-get install build-essential python-dev```</br>
```cd /home/pi```
```git clone https://github.com/adafruit/Adafruit_Python_DHT.git```</br>
```cd Adafruit_Python_DHT```</br>
```sudo python setup.py install```</br>
```cd /home/pi```</br>
```git clone https://github.com/adafruit/Adafruit_Python_BMP.git```</br>
```cd Adafruit_Python_BMP```</br>
```sudo python setup.py install```</br>

<b>Further Information</b>
Wonderground require information to be submitted in specific values e.g.
* Temperature in Farenheit  |  °C  x  9/5 + 32 = °F
* Pressure in barometric pressure inches |  Pa / 33.8638866667
* Dew Point in Farenheit
* Rain in Inches  |  mm * 0.039370
So all reading are converted to required value before uploading.

I will add further as I check and upload my code.


=========================
