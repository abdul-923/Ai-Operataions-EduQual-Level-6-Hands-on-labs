
#!/bin/bash

echo "Welcome to the Logging and Redirecting Output Lab!"
echo "This script demonstrates output management."
echo "Each message will be logged to a file and displayed on the console."

{
  echo "Welcome to the Logging and Redirecting Output Lab!"
  echo "This script demonstrates output management."
  echo "Each message will be logged to a file and displayed on the console."
} | tee output.log
