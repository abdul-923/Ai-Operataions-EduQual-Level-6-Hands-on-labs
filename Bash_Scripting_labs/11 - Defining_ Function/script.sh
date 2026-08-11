

#!/bin/bash

print_greeting() {
  if [ "$2" == "morning" ]; then
    echo "Good Morning, $1!"
  else
    echo "Hello, $1"
    fi
}

print_greeting "$1" "$2"
