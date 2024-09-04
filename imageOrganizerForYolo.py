# coding=utf-8
#!/usr/bin/env python

import argparse
import os
import shutil

global renameCounter

# Parsing inputs and assigning default values to the parameters which are not provided by the user
parser = argparse.ArgumentParser(description='Images reorganizer for Yolo training. This function reorganizes the myDentist image dataset from multiple directories to a single directory.'
	+ 'It takes as an input the path to the directory containing myDentist data.')
parser.add_argument('inFolder', type = str,
					help = 'Path of the directory containing myDentist data.' )
parser.add_argument('outFolder', type = str,
					help = 'Path where to save the myDentist data in a single directory.' )

# entry point of the script
args = parser.parse_args()
inputFolder = args.inFolder
outputFolder = args.outFolder

content = os.listdir(inputFolder)

for element in content:
    print(element + '\n')
    if os.path.isdir(os.path.join(inputFolder, element)):
        subContent = os.listdir(os.path.join(inputFolder, element))
        for subElement in subContent:
            subInputFolder = os.path.join(inputFolder, element)
            if os.path.isfile(os.path.join(subInputFolder, subElement)):
                shutil.copy2(os.path.join(subInputFolder, subElement), os.path.join(outputFolder, subElement))
    elif os.path.isfile(os.path.join(inputFolder, element)):
        shutil.copy2(os.path.join(inputFolder, element), os.path.join(outputFolder, element))
