
##Handling Mulyiple Arguments
#!/bin/bash
# Greet multiple users

if [ $# -eq 0 ]; then
  echo "Usage: ./greet.sh <name1> <name2> ..."
  exit 1
fi

for name in "$@"
do
  echo "Hello, $name!"
done
