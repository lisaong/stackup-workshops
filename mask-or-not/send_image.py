""" Sends an image via Bluetooth to the ESP32
    using Bluetooth Serial Port Profile
"""

#%%
import serial
import numpy as np

#%%
data = np.array([ 53,  60, 168, 182, 180, 161,  60,  30, 197, 211,  12, 119, 178,
       204, 192, 187, 173, 131, 203, 211,  74, 175, 165, 200, 193, 187,
       172, 177, 204, 211, 147, 174, 111,  52, 116, 180,  97, 141, 213,
       211, 141, 178,  89, 157, 175, 184, 157, 175, 210, 211, 139, 176,
       187, 173, 176, 185, 160, 192, 214, 211, 126, 167, 170, 186, 144,
       167, 176, 177, 195, 212, 113, 162, 161, 182, 169, 175, 160, 165,
       219, 212, 154, 146, 163, 159, 157, 165, 149, 160, 213, 213, 219,
       114, 150, 168, 186, 180, 184, 153, 219, 215], dtype=np.uint8)

#%%
# found by ls /dev/cu*
PORT = "/dev/cu.ESP32Bluetooth-ESP32SPP"

with serial.Serial(port=PORT, baudrate=9600) as ser:
    ser.write(bytes(data))

# %%


# %%
