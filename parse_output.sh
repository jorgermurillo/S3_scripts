#!/bin/bash


parse_times(){

        _time_=$1
        _time_=($_time_)
        real_time="${_time_[0]}"
        echo "${_time_[0]}"
}

cnt=0
if [ -p /dev/stdin  ]; then
	
	while IFS= read line; do
		field=$(echo $line  | cut -d ","  -f 1  )
	 	#echo "Line: ${field}"

		if [ $field == "1"  ]; then
			echo "${line}"
		fi
	done
fi
