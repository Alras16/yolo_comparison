import os
import shutil

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
source_dir = os.getcwd() + str(args.source_dir)
subsets = os.listdir(source_dir)

# Path to the framework dataset directory
target_dir = os.getcwd() + str(args.target_dir)

# Load the dublicates directory into the classes to ensure that this directory is also moved
classes.append("Dublicates")

for i in range(0, len(subsets)):
    imgfiles = []
    for j in range(0, len(classes)):
        # Path to the source directory from which the files are moved
        directory = source_dir + subsets[i] + os.sep + classes[j] + os.sep

        # List the files from the source directory
        files = os.listdir(directory)

        # Label and image file directory
        file_dir = target_dir + subsets[i] #+ "/labels/"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        
        # Move the files to the target directory
        for file in files:
            ext = file.split(".")[-1]
            if ext.lower() == 'jpg': # check if file is an image
                shutil.move(directory + file, file_dir)
                imgfiles.append(file)
            elif ext.lower() == 'txt':
                shutil.move(directory + file, file_dir)
            else:
                continue

    # Load all image files into the images textfile
    datafile_dir = target_dir + os.sep + subsets[i] + ".txt"
    with open(datafile_dir, 'w') as images_file:
        for file in imgfiles:
            images_file.write("build/darknet/x64/data/obj/" + file + "\n")
    images_file.close()

# Remove the OID folder inside the OIDv4 toolkit
oid_path = source_dir.rsplit('/', 2)[0] + os.sep
if os.path.exists(oid_path): 
    shutil.rmtree(oid_path)
