import argparse

# -*- coding: utf-8 -*-
# requires: pip install paho-mqtt
import paho.mqtt.client as mqtt

class MqttIpClient:
    def __init__(self, mac_addresses):
        self.mac_addresses = mac_addresses

    def subscribe(self):
        client = mqtt.Client()
        client.user_data_set(self.mac_addresses)
        client.on_connect = MqttIpClient.on_connect
        client.on_message = MqttIpClient.on_message

        client.connect('iot.eclipse.org', 1883, 60)
        print('Subsribed')
        client.loop_forever()

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if type(userdata) != list:
            raise TypeError('Invalid type for userdata')

        mac_addresses = userdata
        for m in mac_addresses:
            client.subscribe(f'pybmt/{m.rstrip()}/wlan0')

    @staticmethod
    def on_message(client, userdata, msg):
        print(f'{msg.topic} {str(msg.payload)}')

parser = argparse.ArgumentParser()
parser.add_argument('mac_address_file',
    type=argparse.FileType('r', encoding='utf-8'))

args = parser.parse_args()
mac_addresses = args.mac_address_file.readlines()
args.mac_address_file.close()

client = MqttIpClient(mac_addresses)
client.subscribe()