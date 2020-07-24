""" Sends an image via Bluetooth to the ESP32
    using Bluetooth Serial Port Profile
"""

#%%
import serial

#%%
with serial.Serial(port='COM7', baudrate=9600) as ser:
    ser.open()
    ser.write(123)

# %%
