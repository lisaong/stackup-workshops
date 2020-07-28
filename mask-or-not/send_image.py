""" Sends an image from webcam via Bluetooth to the ESP32
    using Bluetooth Serial Port Profile
"""

#%%
import serial
import numpy as np
import matplotlib.pyplot as plt
import cv2

#%%
face_cascade = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_eye.xml')

def crop_face(img, output_size=(10, 10)):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  height, width, channels = img.shape

  # use the colour version for detection, but the
  # grayscale version for result
  faces = face_cascade.detectMultiScale(img)
  eyes = eye_cascade.detectMultiScale(img)

  face = None
  if len(faces) > 0:
    x,y,w,h = faces[0]
    face = gray[y:y+h, x:x+w]
  elif len(eyes) > 0:
    # mask is stumping haar face detection
    # approximate face by detecting the left eye
    x,y,w,h = eyes[0]
    # approximate face dimensions using the
    # left eye as reference
    face = gray[max(0, y-2*h):min(y+4*h, height), 
                max(0, x-3*w):min(x+2*w, width)]
  else:
    # nothing detected, just return original image
    face = gray

  face = cv2.resize(face, output_size)
  return face

#%%
# capture face using webcam
input('Press Enter to Capture')

video_capture = cv2.VideoCapture(0)

if not video_capture:
  # On MacOS, this should be run inside terminal, or launch VSCode from terminal.
  print('Unable to load camera. Please check if the camera is connected or if you have permissions to open it.')
  exit(-1)

ret, frame = video_capture.read()
cv2.imshow('Captured face', frame)
cv2.waitKey(0)

video_capture.release()
cv2.destroyAllWindows()

#%%
data = crop_face(frame)
plt.imshow(data, cmap='gray')
plt.title('Pre-processed face')
plt.show()

#%%
# sample data if camera capture is not working
#data = np.array([ 53,  60, 168, 182, 180, 161,  60,  30, 197, 211,  12, 119, 178,
#       204, 192, 187, 173, 131, 203, 211,  74, 175, 165, 200, 193, 187,
#       172, 177, 204, 211, 147, 174, 111,  52, 116, 180,  97, 141, 213,
#       211, 141, 178,  89, 157, 175, 184, 157, 175, 210, 211, 139, 176,
#       187, 173, 176, 185, 160, 192, 214, 211, 126, 167, 170, 186, 144,
#       167, 176, 177, 195, 212, 113, 162, 161, 182, 169, 175, 160, 165,
#       219, 212, 154, 146, 163, 159, 157, 165, 149, 160, 213, 213, 219,
#       114, 150, 168, 186, 180, 184, 153, 219, 215], dtype=np.uint8)

#%%
# found by ls /dev/cu*
PORT = "/dev/cu.ESP32Bluetooth-ESP32SPP"

with serial.Serial(port=PORT, baudrate=9600) as ser:
    ser.write(bytes(data))

# %%
