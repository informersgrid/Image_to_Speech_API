# Image_to_Speech_API

## Setup
Follow the steps below to setup and use the project.

### Step 1: Download the source code
Download the Image_to_Speech_API.zip file and extract the contents.
(If you are confortable with *GIT* then use the `git clone https://github.com/informersgrid/Image_to_Speech_API.git` on the Terminal)

### Step 2: Install the following dependencies for Linux
#### Python
All the scripts are written in Python and need python to be installed.
Refer to: http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/

#### PIP
PIP package manager is required to install the dependencies for the python scripts.
Refer to: https://www.tecmint.com/install-pip-in-linux/

#### Tesseract 4.0 OCR
In the Terminal, type the following commands(type the user account password if prompted):
```sh
sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo pip install pytesseract
```
In case it doesn't work, refer to https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/ for more instructions

#### Google Text-to-Speech
In the Terminal, type the following command:
```sh
pip install gTTS
```

#### MP3 Player
In the Terminal, type the following command:
```sh
sudo apt-get install mpg321
```

In case it doesn't work refer to https://www.geeksforgeeks.org/convert-text-speech-python/ for more instructions

### Step 3: Setup for Raspberry Pi Camera
Open the Terminal application and navigate to the Image_to_Speech_API folder using `cd <path>` command.
To check if the Raspberry Pi camera is working, run the following commands in the Terminal:
```sh
cd raspi_setup
python raspi_camera_test.py
```
If the camera is functional then an image file with the name *raspi_camera_image.jpg* will appear on the Raspberry Pi desktop in 10 seconds.

If there are any issues, refer here : https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

If the *pycamera* python package is not installed, then it must be installed by referring to : https://picamera.readthedocs.io/en/release-1.13/install.html

## How to use the API ?
### Using with image file input
Open a command line terminal and navigate to the folder *Image_to_Speech_API*

Use the following command syntax to run the python script:
```sh
python image-text-speech.py <image_file_path> <output_audio_filename>
```
Example 1:
```sh
python image-text-speech.py sample_images/textbook-page.webp textbook-page-audio.mp3
```
Example 2:
```sh
python image-text-speech.py sample_images/street-signs.png street-signs-audio.mp3
```
The script will process the *<image_file_path>* image, save the audio onto the mp3 format audio file *<output_audio_filename>* and start playing the audio.
 

### Using with Raspberry Pi Camera image input
Open a command line terminal and navigate to the folder *Image_to_Speech_API*

Use the following command syntax to run the python script:
```sh
python raspi_image_to_speech.py [<number_of_images>]
```
Example 1: To take an image and convert to speech once
```sh
python raspi_image_to_speech.py
```
Example 2: To take an image and convert to speech for 10 times
```sh
python raspi_image_to_speech.py 10
```
[<number_of_images>] is optional. By default it will convert the Raspberry Pi camera image to speech one time.
