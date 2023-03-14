#!/bin/bash

arr=( 8 4 2 1 3 0 2)

echo "Length of the array - ${#arr[@]} "  

# Using for loop to find the max and min element.
echo "Max and Min of the array using for loop"


max=${arr[0]} #Assuming first element as max

for n in "${arr[@]}" ; do
    if [ $n -ge $max ]; then 
		max=$n
	fi
done
echo "Maximum in the array - $max"


min=${arr[0]} #Assuming first element as min
for n in "${arr[@]}" ; do
    if [ $n -le $min ]; then 
    	min=$n
	fi
done

echo "Minimum in the array - $min"