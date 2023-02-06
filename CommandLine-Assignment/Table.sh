#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Please enter arguments to generate table!!!"
  exit 1
fi

i=1;
j=$#;
while [ $i -le $j ] 
do
	n=$1 
	c=1
	echo "Table of $n:"

	while [ $c -le 10 ] 
	do
	  result=$(( $n * $c ))
	  echo "$n x $c = $result" 
	  c=$(( $c + 1 ))
	done
    shift 1;
	i=$((i+1))
	echo ""
done

exit 0