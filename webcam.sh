#!/bin/bash
# Last updated: 2016-10-27
# Created by Benjamin Harris

# Requires fswebcam and functioning webcamera
# sudo apt-get install -y ftp
# sudo apt-get install -y fswebcam
# sudo apt-get install -y ncftpput
# */5 * * * * /path/to/webcam.sh >> /dev/null 2>&1
# Tested on Raspberry PI running Raspian and Logitech Webcamera
# You may have to change fswebcam options to match you camera

# ===========================================================
# Configuration options
# ===========================================================

# Time between uploading images to wunderground
delay = 600
# Wunderground personal weather station ID/password
stationid = id
password = password
ftphost = webcam.wunderground.com

# ===========================================================
# Begin Script
# ===========================================================

filename=`date +'%F-%H-%M'`.jpg

cd webcamuploads
fswebcam -D 1 -S 3 -p MJPEG -r 1024x768 --jpeg 95 --no-banner /dev/null -F 3
sleep 2
fswebcam -D 1 -S 3 -p MJPEG -r 1024x768 --jpeg 95 --no-banner --save ${filename}
cp ${filename} image.jpg

/usr/bin/ftp -v -n $ftphost <<EOF
user $stationid $password
binary
put image.jpg

quit

EOF

# removes date image file
rm ${filename}
