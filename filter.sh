#!/bin/bash


if [ -p /dev/stdin  ]; then
	
	while IFS= read line; do
		field=$(echo $line  | cut -d ","  -f 1  )
	 	#echo "Line: ${field}"

		if [ $field == "1"  ]; then
			echo "${line}"
		fi
	done
fi
