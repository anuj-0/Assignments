#!/bin/bash

# check_prime() checks if a number is prime or not
function check_prime() {
  n=$1 
  if [ $n -lt 2 ]; then
    echo "$n is not a prime number."
    return
  fi
  for (( i=2; i<$(($n/2+1)); i++ ))
  do
    if [ $(($n%$i)) -eq 0 ]; then
      echo "$n is not a prime number."
      return
    fi
  done
  echo "$n is a prime number."
}

#Taking input from the user
read -p "Number : " n
check_prime $n

exit 0