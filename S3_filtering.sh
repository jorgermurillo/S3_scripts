#!/bin/bash
bucket=$1
parse_times(){

	_time_=$1
	_time_=($_time_)
	real_time="${_time_[0]}"
	echo "${_time_[0]}"
}

declare -a StringArray=("100000"  "500000" "750000"  "1000000" "2000000")

for val in ${StringArray[@]};do
	echo $val

	time  python3 S3_print_object.py $bucket   $val | ./split_simple >  /dev/null 
	#parse_times "$tmp"
done   



