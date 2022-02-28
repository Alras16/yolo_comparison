import os
import glob
import shutil
import os.path

from tqdm import tqdm
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
subsets = os.listdir(os.getcwd() + str(args.source_dir))

files, dublicates = [], []
for k in range(0, len(subsets)):
    # Path to directory
    dir_path = os.getcwd() + str(args.source_dir) + subsets[k]

    count = 0
    for l in range(0, len(classes)):
        # Path to class subdirectory
        subdir_path = os.path.join(dir_path, classes[l])

        # Remove the label subdirectory under each class
        label_subdir = os.path.join(subdir_path, "Label")
        if os.path.exists(label_subdir): 
            shutil.rmtree(label_subdir)

        # Load all txt files in the directory into a list
        for file in glob.glob(subdir_path + os.sep + "*.jpg"):
            filename = file.split(os.sep)[-1] # separate path from filename
            if files.count(filename) > 0: # check if filename exists in list
                name, ext = filename.split(".")
                if not dublicates.count(name) > 0: # check if name do not exist in list
                    dublicates.append(name) # if so append it to a list of dublicates
                    count += 1
            else:
                files.append(filename) #if not append it to a list of filenames
                continue  
    
    #print(f"Number of dublicates: {count}")

    # Create directory to contain merged dublicates
    dub_dir = os.path.join(dir_path, "Dublicates") + os.sep
    if not os.path.exists(dub_dir):
        os.makedirs(dub_dir)

    # Check if there are any files with the same name
    if count > 0:
        # Find the path to all dublicated files
        imgs, labels = [], []
        for filename in dublicates:
            path = dir_path + "/**/" + filename + ".txt"
            files = glob.glob(path, recursive=True)
            if len(files) > 1: # Check if files contains more than one filepath 
                # Create a list of dublicated label files
                labels.append(files)

                # Create a list of dublicated image files as well
                imgfiles = []
                for file in files:
                    img = file.split(".")[0] + ".jpg"
                    imgfiles.append(img)
                imgs.append(imgfiles)
        
        #print(f"Number of image files: {len(imgs)}")
        #print(f"Number of label files: {len(labels)}")

        if (len(labels) == len(imgs) and len(imgs) > 0):
            for i in tqdm(range(0, len(imgs)), desc=f"Move the {count} dublicates in {subsets[k]}"):
                # Merge the label files into one in the dublicates directory
                label_file = dub_dir + labels[i][0].split(os.sep)[-1]
                with open(label_file, 'w') as outfile:
                    for label in labels[i]:
                        with open(label, 'r') as file:
                            outfile.write(file.read())
                        os.remove(label) # delete the label
                # Move image file into the dublicates directory 
                # and delete the rest of the images
                shutil.move(imgs[i][0], dub_dir)
                imgs[i].pop(0)
                for img in imgs[i]:
                    os.remove(img)    
        else:
            print(f"The number of dublicated images and labels are not equals or equal to zero.")