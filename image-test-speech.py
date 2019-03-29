# Import the required module for image to text  to speech conversion 
from gtts import gTTS 
import cv2
import sys
import pytesseract
# This module is imported so that we can  
# play the converted audio 
import os
 
if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Usage: python image-text-speech.py input_image.jpg output_audio.mp3')
		sys.exit(1)

	# Read image path from command line
	imPath = sys.argv[1]

	# Uncomment the line below to provide path to tesseract manually
	# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

	# Define config parameters.
	# '-l eng'  for using the English language
	# '--oem 1' for using LSTM OCR Engine
	config = ('-l eng --oem 1 --psm 3')

	# Read image from disk
	im = cv2.imread(imPath, cv2.IMREAD_COLOR)

	# Run tesseract OCR on image
	text = pytesseract.image_to_string(im, config=config)

	# Print recognized text
	print(text)

	# Google Text to Speech 

	# The text that you want to convert to audio 
	mytext = text
	  
	# Language in which you want to convert 
	language = 'en'
	  
	# Passing the text and language to the engine,  
	# here we have marked slow=False. Which tells  
	# the module that the converted audio should  
	# have a high speed 
	myobj = gTTS(text=mytext, lang=language, slow=False) 
	 
	# Read image path from command line
	output_audio = sys.argv[2]

	# Saving the converted audio in a mp3 file
	myobj.save(output_audio) 
	  
	# Playing the converted file 
	os.system("mpg321 "+output_audio) 

