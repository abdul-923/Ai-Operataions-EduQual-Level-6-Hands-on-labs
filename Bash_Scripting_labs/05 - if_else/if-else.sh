
#!bin/bash

echo "Enter the file name: "
read FILENAME

if [ -f "$FILENAME" ]; then
  echo "File exists"
else
  echo "File not Found. "

fi
