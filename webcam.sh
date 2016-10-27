# Last updated: 2016-10-27
# Created by Benjamin Harris

# Requires fswebcam and functioning webcamera

# Tested on Raspberry PI running Raspian and Logitech Webcamera
# You may have to change fswebcam options to match you camera

# ===========================================================
# Configuration options
# ===========================================================

# Time between uploading images to wunderground
delay = 600
# Wunderground personal weather station ID/password
stationid = ""
password = ""
ftphost = "webcam.wunderground.com"

# ===========================================================
# Begin Script
# ===========================================================

filename=`date +'%F-%H-%M-%S'`.jpg

cd webcamuploads
fswebcam -p MJPEG -r 1280x720 --jpeg 95 --no-banner --save ${filename}
cp ${filename} image.jpg

ftp -n ftphost <<EOF
user stationid password
binary
put image.jpg

quit

EOF
