import os
import glob
import argparse

from scripts.parser import *

args = parser_arguments()

# Read the classes from the class text file.
if args.classes is not None:
    file = open(os.getcwd() + str(args.class_file), 'w')
    classes = [line.replace("_", " ") for line in args.classes]
    names = [element + "\n" for element in classes]
    file.writelines(names)
else:
    file = open(os.getcwd() + str(args.class_file), 'r')
    classes = [line.rstrip().replace("_", " ") for line in file.readlines()]

# Path to the OID dataset directory
subsets = os.listdir(os.getcwd() + str(args.dataset_dir))

for i in range(0, len(subsets)):
    print("\n")
    print(f"{subsets[i]} subset:")
    print("\n")
    for j in range(0, len(classes)):
        # Path to directory
        directory = os.getcwd() + str(args.dataset_dir) + subsets[i] + os.sep + classes[j] + "/Label/"

        # Load all txt files in the directory into a list
        txtfiles = []
        for file in glob.glob(directory + "*.txt"):
            txtfiles.append(file)

        # Count the number of objects in the txt files
        objects = 0
        for file in txtfiles:
            f = open(file, "r")
            for line in f:
                if line != "\n":
                    objects += 1
            f.close()

        print(f"Number of {classes[j]} object instances: {objects}")
    