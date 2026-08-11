

#!/bin/bash

fruits=("Apple" "Banana" "Mango")


echo "Fruits array: ${fruits[@]}"

echo " Iterating over each element"

for fruit in "${fruits[@]}"; do
  echo "Fruits: $fruit"

done

echo "Adding element(Grapes)"

fruits+=("Grapes")

echo "Updated Array: ${fruits[@]}"
