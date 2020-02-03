import sys
import netifaces as ni
import paho.mqtt.client as mqtt

if len(sys.argv) < 4:
    print(f'Usage: {sys.argv[0]} interface mqtt_server_url port')
    exit(-1)

interface = sys.argv[1]
mqtt_host = sys.argv[2]
mqtt_port = int(sys.argv[3])

addresses = ni.ifaddresses(interface)
mac_address = addresses[ni.AF_LINK][0]['addr']
ip_address = addresses[ni.AF_INET][0]['addr']

# publish to MQTT
topic = f'pybmt/{mac_address}/{interface}'

mqttc = mqtt.Client()
mqttc.connect(mqtt_host, mqtt_port)
print(f'connected to {mqtt_host}:{mqtt_port}')

mqttc.publish(topic, ip_address)
print(f'published to {topic}: {ip_address}')
