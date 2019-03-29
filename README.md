# Image_to_Speech_API

## Install the following dependencies for Linux
### Python
All the scripts are written in Python and need python to be installed.
Refer to: http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/

### PIP
PIP package manager is required to install the dependencies for the python scripts.
Refer to: https://www.tecmint.com/install-pip-in-linux/

### Tesseract 4.0 OCR
```
sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo pip install pytesseract
```
In case it doesn't work, refer to https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/ for more instructions

### Google Text-to-Speech
`pip install gTTS`

In case it doesn't work refer to https://www.geeksforgeeks.org/convert-text-speech-python/ for more instructions

## Setup for Raspberry Pi Camera
Refer here : https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

If pycamera is not installed then refer to : https://picamera.readthedocs.io/en/release-1.13/install.html

Sample python code:
```
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(5):
  sleep(10)
  camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
```
## How to use the API
### Download
Download the Image_to_Speech_API.zip file and extract the contents.

### Usage
Open a command line terminal and go to the folder Image_to_Speech_API.zip

Run the following command:
`python image-text-speech.py <name_of_image_file> <name_of_output_audio>`


