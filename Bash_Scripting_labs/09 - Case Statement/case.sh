
#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage : $0 {Start | Stop | Status}"
  exit 1

fi

case $1 in
  start)
    echo "Starting Services..."
    ;;
  stop)
    echo "Stopping Services..."
    ;;
  status)
    echo "Checking Status..."
    ;;
  *)
    echo "Invalid Command"

esac
