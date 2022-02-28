#!/bin/bash
# Choose how many and which classes to download among the 600 classes in the Open Images V4 dataset.
read -p "Number of classes: " nclasses
names = ""
echo "Enter name of each of the ${classes} classes: "
for (( counter>0; counter<classes+1; counter++ )); do
    read -p "${counter} " -a name
    names+="$name "
done

# Clone the OIDv4 ToolKit github repository and enter the directory.
git clone https://github.com/theAIGuysCode/OIDv4_ToolKit.git
cd OIDv4_ToolKit 

# Choose which subset of the Open Images V4 dataset should be downloaded.
echo ""
while true; do
    read -p "What subsets do you want to download? (train, validation, test, all): " csv
    case $csv in
        [validation]* ) python3 main.py downloader --classes $names --type_csv $csv; break;;
        [train]* ) python3 main.py downloader --classes $names --type_csv $csv; break;;
        [test]* ) python3 main.py downloader --classes $names --type_csv $csv; break;;
        [all]* ) python3 main.py downloader --classes $names --type_csv $csv; break;;
        * ) echo "Please answer either train, validation, test or all.";;
    esac
done



# Convert the labels to YOLO format
python3 convert_annotations.py