# Import the required module for image to text  to speech conversion 
from gtts import gTTS 
import cv2
import sys
import pytesseract
# This module is imported so that we can  
# play the converted audio 
import os
# Raspberry Pi
from picamera import PiCamera
from time import sleep

if __name__ == '__main__':
	num_repeat=1
	if len(sys.argv) = 2:
		num_repeat=sys.argv[1]
	
	print('Executing '+num_repeat+' times');

	camera = PiCamera()

	camera.start_preview()
	for i in range(num_repeat):
		camera.capture('/home/pi/Desktop/raspi_camera_image.jpg')

		# Playing the converted file 
		os.system("python image-text-speech.py /home/pi/Desktop/raspi_camera_image.jpg raspi_audio.mp3") 


		sleep(5)
	camera.stop_preview()