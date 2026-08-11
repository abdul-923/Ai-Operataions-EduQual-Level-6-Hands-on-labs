

#!/bin/bash

echo "Enter a String: "
read user_input
echo "you entered: $user_input"


length=${#user_input}
echo "The lenght is: $length"


substring=${user_input:2:4}
echo "Substring from position 2 to 5 is: $substring"

