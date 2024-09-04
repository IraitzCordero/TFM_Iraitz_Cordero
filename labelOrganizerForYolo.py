# coding=utf-8
#!/usr/bin/env python

import argparse
import os
import shutil

global renameCounter

# Parsing inputs and assigning default values to the parameters which are not provided by the user
parser = argparse.ArgumentParser(description='Labels reorganizer for Yolo training. This function finds labels into the myDentist image dataset moving them to the selected labels directory.'
	+ 'It takes as an input the path to the directory containing myDentist data\'s labels and the path to the Yolo\'s train/test/validation images directory.')
parser.add_argument('labelsFolder', type = str,
					help = 'Path of the directory containing myDentist data\'s labels.' )
parser.add_argument('imagesFolder', type = str,
					help = 'Yolo\'s path where are train/validation/test images directory to save there the associated labels in /labels directory.')

# entry point of the script
args = parser.parse_args()
labelsFolder = args.labelsFolder
imagesFolder = args.imagesFolder

os.mkdir(os.path.join(imagesFolder, 'labels'))
outputFolder = os.path.join(imagesFolder, 'labels')

labels = os.listdir(labelsFolder)
images = os.listdir(imagesFolder)

for label in labels:
	labelName, extension = os.path.splitext(label)
	print(labelName + '\n')
	for image in images:
		if os.path.isfile(os.path.join(imagesFolder, image)):
			imageName, extension = os.path.splitext(image)
			if (imageName == labelName):
				shutil.move(os.path.join(labelsFolder, label), os.path.join(outputFolder, label))
