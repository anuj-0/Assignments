#!/bin/bash


mkdir -p ~/Desktop/Assignment
echo "Assignment Folder created on the Desktop."

touch -a ~/Desktop/Assignment/File1.txt
echo "File1.txt created in Assignment Folder."

cat ~/Desktop/Table.sh  >> ~/Desktop/Assignment/File1.txt
echo "Data in Table.sh copied to File1.txt."

echo "Welcome to Sigmoid" >> ~/Desktop/Assignment/File1.txt

echo "Folders in the Desktop:"
ls -la ~/Desktop/

exit 0