import argparse

# -*- coding: utf-8 -*-
# requires: pip install paho-mqtt
import paho.mqtt.client as mqtt

class MqttIpClient:
    def __init__(self, mac_addresses, interface):
        self.mac_addresses = mac_addresses
        self.interface = interface

    def subscribe(self):
        client = mqtt.Client()
        client.user_data_set(self)
        client.on_connect = MqttIpClient.on_connect
        client.on_message = MqttIpClient.on_message

        client.connect('mqtt.eclipse.org', 1883, 60)
        print(f'Subscribed for {self.interface}')
        client.loop_forever()

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if type(userdata) != list:
            raise TypeError('Invalid type for userdata')

        self_obj = userdata
        for m in self_obj.mac_addresses:
            client.subscribe(f'pybmt/{m.rstrip()}/{self_obj.interface}')

    @staticmethod
    def on_message(client, userdata, msg):
        print(f'{msg.topic} {str(msg.payload)}')

parser = argparse.ArgumentParser()
parser.add_argument('mac_address_file',
    type=argparse.FileType('r', encoding='utf-8'))
parser.add_argument('--interface')

args = parser.parse_args()
mac_addresses = args.mac_address_file.readlines()
args.mac_address_file.close()

interface = 'wlan0'
if args.interface is not None:
    interface = args.interface

client = MqttIpClient(mac_addresses, interface)
client.subscribe()
