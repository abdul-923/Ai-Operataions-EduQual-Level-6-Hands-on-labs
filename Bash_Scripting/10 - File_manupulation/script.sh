
#!/bin/bash

SOURCE=$1
DESTINATION=$2

if [ -z "$SOURCE" ] || [ -z "$DESTINATION" ]; then
  echo " Argument Missing "
  exit 1
fi

if [ ! -f "$SOURCE" ]; then
  echo " Error: Source file not exist. "
  exit 1
fi

cp "$SOURCE" "$DESTINATION"

if [ $? -eq 0 ]; then
  echo "File copied successfully to '$DESTINATION'."
else
  echo "Error in Copying file."
fi
