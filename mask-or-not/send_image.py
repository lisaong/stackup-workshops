""" Sends an image via Bluetooth to the ESP32
    using Bluetooth Serial Port Profile
"""

#%%
import serial

#%%
# found by ls /dev/cu*
PORT = "/dev/cu.ESP32Bluetooth-ESP32SPP"

with serial.Serial(port=PORT, baudrate=9600) as ser:
    ser.write(123)

# %%
