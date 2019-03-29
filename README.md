# Image_to_Speech_API

## Install the following dependencies for Linux
### Tesseract 4.0 OCR
sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo pip install pytesseract

In case it doesn't work, refer to https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/ for more instructions

### Google Text-to-Speech
pip install gTTS

In case it doesn't work refer to https://www.geeksforgeeks.org/convert-text-speech-python/ for more instructions

## For Raspberry Pi Camera
Refer here : https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

Sample python code:
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(5):
  sleep(10)
  camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

