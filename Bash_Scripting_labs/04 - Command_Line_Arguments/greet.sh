

#!/bin/bash
# Greet the user by name

if [ -z "$1" ]; then
  echo "Usage: ./greet.sh <name>"
  exit 1
fi

name=$1
echo "Hello, $name!"
