# coding=utf-8
#!/usr/bin/env python

import argparse
import os
import shutil

global renameCounter

# Parsing inputs and assigning default values to the parameters which are not provided by the user
parser = argparse.ArgumentParser(description='Image and each associated label tester and vice versa. This function tests if a image has a associated label and vice versa.'
	+ 'It takes as an input the path of the labels directory and the path of the images directory.')
parser.add_argument('labelsFolder', type = str,
					help = 'Path of the labels directory.' )
parser.add_argument('imagesFolder', type = str,
					help = 'Path of the images directory.')

# entry point of the script
args = parser.parse_args()
labelsFolder = args.labelsFolder
imagesFolder = args.imagesFolder

labels = os.listdir(labelsFolder)
images = os.listdir(imagesFolder)

print('\nStarting...\n')

for label in labels:
	labelName, extension = os.path.splitext(label)
	match = False
	for image in images:
		if os.path.isfile(os.path.join(imagesFolder, image)):
			imageName, extension = os.path.splitext(image)
			if (labelName == imageName):
				match = True
	if match is False:
		print('\n' + labelName + ' label doesn\'t have an image associated.')

print('\n')

# This block doesn't works well

#for image in images:
#	imageName, extension = os.path.splitext(image)
#	match = True
#	for label in labels:
#		if os.path.isfile(os.path.join(labelsFolder, label)):
#			labelName, extension = os.path.splitext(label)
#			print('img: ' + imageName + '\n')
#			print('label: ' + labelName + '\n\n')
#			if (imageName != labelName):
#				match == False
#	if match is True:
#		#print('\n' + imageName + ' image doesn\'t have a label associated.')
#		kaka = 'i'

print('\nCompleted.')
