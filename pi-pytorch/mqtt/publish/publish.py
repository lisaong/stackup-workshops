import sys
import netifaces as ni

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} interface mqtt_server_url')
    exit(-1)

interface = sys.argv[1]
mqtt_host = sys.argv[2]

print(ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])

"""
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
"""
