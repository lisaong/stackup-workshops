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
cv2.imwrite('frame.png', frame)

video_capture.release()
cv2.destroyAllWindows()

#%%
data = crop_face(frame)
plt.imshow(data, cmap='gray')
plt.title('Pre-processed face')
plt.show()

#%%
# sample data if camera capture is not working
test_data_no_mask = np.array([176,  37,  61, 112, 111,  92,  33,  29,  26,  76,  48,  24, 115,
       119, 115, 116,  81,  26,  23,  32,  51,  34, 103, 104, 108,  87,
        49,  60,  19,  30,  75,  57, 106,  58,  47,  80,  56,  31,  24,
        26,  27,  49,  90,  66,  91,  54,  82,  95,  62,  16,  15, 187,
       116, 108, 165, 108, 107, 122, 111,  18,  14, 192, 159, 109, 123,
        94, 114, 123,  94,  22,  19, 161, 167, 173, 146, 118, 112, 106,
        54,  22,  93,  30, 171, 115, 119,  94,  84, 100,  50,  27, 193,
       177, 205, 142, 133, 105, 108,  99,  57,  48], dtype=np.uint8)

test_data_mask = np.array([166,  41,  28, 106,  98,  93,  40,  21,  28,  63, 164,  37, 119,
       125, 101, 100,  89,  18,  20, 203, 125,  13, 141,  48,  66,  55,
        48,  59,  23,  28,  50,  27,  56,  42,  83,  53,  53,  63,  28,
        18,  64,  21, 164, 169, 241, 189, 181, 185, 189,  16,  19, 107,
       250, 241, 220, 199, 194, 194, 207,  13,  82,  40, 247, 238, 242,
       194, 197, 200, 201,  57,  66,  68, 204, 223, 231, 188, 195, 183,
        19,  33,  56, 204, 173, 196, 210, 167, 178, 159,  53,  62, 103,
       192, 161, 133, 125,  69,  73,  89,  84,  62], dtype=np.uint8)

# set this for testing to override camera image
# data = test_data_no_mask

#%%
# found by ls /dev/cu*
PORT = "/dev/cu.ESP32Bluetooth-ESP32SPP"

with serial.Serial(port=PORT, baudrate=9600) as ser:
    ser.write(bytes(data))

# %%

