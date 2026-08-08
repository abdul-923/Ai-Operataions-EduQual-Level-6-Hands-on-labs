

#!/bin/bash


echo "Enter Your First Number"
read num1

echo "Enter Your Second Number"
read num2


echo "Addition: "
sum=$((num1 + num2))
echo "The Sum is: $sum"


echo "Subtraction"
subt=$((num1 - num2))
echo "The Subtraction is: $subt"

echo "Multiplication: "
mult=$((num1 * num2))
echo "Multiplication is: $mult"

echo "Using bc"
subt_bc=$(echo "$num1 * $num2" | bc)
echo "The bc is: $subt_bc"


echo "Division"

if [ "$num2" -ne 0 ]; then
    quotient=$((num1 / num2))
    echo "The Division is: $quotient"
else
    echo "Division by zero is not allowed."
fi
