# coding=utf-8
#!/usr/bin/env python

import argparse
import os
import shutil

global imageCounter
global patientCounter

# Parsing inputs and assigning default values to the parameters which are not provided by the user
parser = argparse.ArgumentParser(description='Data reorganizer for myDentist Dataset. This function reorganizes and renames data from directories.'
    + 'It takes as an input the path to the directory containing myDentist data.')
parser.add_argument('inFolder', type = str,
                    help = 'Path of the directory containing myDentist data.' )
parser.add_argument('outFolder', type = str,
                    help = 'Path where to save the reorganized and renamed myDentist data.' )
parser.add_argument('-mode', '--mode', default='separated', type=str, help='The mode of data reorganization (default: separated).\n In case of <<-mode joined>> data for all the subdirectories will be joined, in case of <<-mode separated>> not.')
parser.add_argument('-imageCounter', '--imageCounter', default=1, type=int, help='The image counter to rename the data (default: 1).')
parser.add_argument('-patientCounter', '--patientCounter', default=1, type=int, help='The patient counter to rename the data (default: 1).')

# entry point of the script
args = parser.parse_args()
inputFolder = args.inFolder
outputFolder = args.outFolder
reorganizationMode = args.mode
imageCounter = args.imageCounter
patientCounter = args.patientCounter

digits = len(str(patientCounter))
if (digits == 1):
    patientFolder = '0000' + str(patientCounter)
elif (digits == 2):
    patientFolder = '000' + str(patientCounter)
elif (digits == 3):
    patientFolder = '00' + str(patientCounter)
elif (digits == 4):
    patientFolder = '0' + str(patientCounter)
elif (digits == 5):
    patientFolder = str(patientCounter)

content = os.listdir(inputFolder)

for element in content:
    print(element + '\n')
    if os.path.isdir(os.path.join(inputFolder, element)):
        os.mkdir(os.path.join(outputFolder, patientFolder))
        subContent = os.listdir(os.path.join(inputFolder, element))
        for subElement in subContent:
            subInputFolder = os.path.join(inputFolder, element)
            subOutputFolder = os.path.join(outputFolder, patientFolder)
            if os.path.isfile(os.path.join(subInputFolder, subElement)):
                root, extension = os.path.splitext(subElement)
                shutil.copy2(os.path.join(subInputFolder, subElement), os.path.join(subOutputFolder , subElement))
                os.rename(os.path.join(subOutputFolder, subElement), os.path.join(subOutputFolder, "image" + str(imageCounter) + extension))
                imageCounter += 1
        patientCounter += 1
        digits = len(str(patientCounter))
        if (digits == 1):
            patientFolder = '0000' + str(patientCounter)
        elif (digits == 2):
            patientFolder = '000' + str(patientCounter)
        elif (digits == 3):
            patientFolder = '00' + str(patientCounter)
        elif (digits == 4):
            patientFolder = '0' + str(patientCounter)
        elif (digits == 5):
            patientFolder = str(patientCounter)
    elif os.path.isfile(os.path.join(inputFolder, element)):
        root, extension = os.path.splitext(element)
        shutil.copy2(os.path.join(inputFolder, element), os.path.join(outputFolder, element))
        os.rename(os.path.join(outputFolder, element), os.path.join(outputFolder, "image" + str(imageCounter) + extension))
        imageCounter += 1

info = open(os.path.join(outputFolder, 'info.txt'), 'w+')
info.write('Last patient: ' + str(patientCounter - 1) +'\nLast image: image' + str(imageCounter - 1))
