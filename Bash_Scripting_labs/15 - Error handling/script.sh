

#!/bin/bash 

directory=/home/ubuntu/Ai-Operataions-EduQual-Level-6-Hands-on-labs/Bash_Scripting

if [ -d "$directory" ]; then
  echo "Directory Exist. "

else 
  echo "Error: Directory not exist. "
  echo "Please Create a Directory first. "
  exit 1

fi


