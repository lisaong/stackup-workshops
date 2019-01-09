
#! /bin/bash

# mqttmyip.sh
# Posts the IP address of an interface to an MQTT queue
# Credits: Simen Sommerfeldt, based on work by San Bergmans (www.sbprojects.net)
# https://sommerfeldt.co/2015/10/10/using-mqtt-to-get-that-friggin-ip-address-from-the-raspberry-pi-on-boot/
#
# Pre-requisites:
# sudo apt-get install mosquitto mosquitto-clients
#
# To run on boot, edit /etc/rc.local script to add this line (before 'exit 0').
#
# /home/pi/mqttmyip.sh &
#

# Configuration variables

# MQTT broker. If this isn´t up check https://github.com/mqtt/mqtt.github.io/wiki/public_brokers
MQTTHOST="iot.eclipse.org"
IFC="wlan0"
MAC=`cat /sys/class/net/$IFC/address`

# Change this to become something unique, so that you get your own topic path
MQTTPREFIX="pybmt"

# Get current private IP address for the selected interface
PRIVATE=$(ifconfig $IFC | grep "inet " | awk '{ print $2 }')

# Exit if IP address is empty
if [ -z $PRIVATE ]
then
 exit 0
fi

/usr/bin/mosquitto_pub -h $MQTTHOST -t "$MQTTPREFIX/$MAC/$IFC" -m "$PRIVATE"
