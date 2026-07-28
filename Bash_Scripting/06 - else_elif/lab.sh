
#!/bin/bash

echo "Enter Your Number:"
read number

if [ -z "$number" ]; then
  echo "Empty"
  exit 1

elif [ "$number" -gt 10 ]; then
  echo "Above 10"

elif [ "$number" -eq 10 ]; then
  echo "Exactly 10"

else 
  echo "Below 10"

fi
