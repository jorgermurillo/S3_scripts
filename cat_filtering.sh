#!/bin/bash


declare -a StringArray=("100000"  "500000" "750000"  "1000000" "2000000")

for val in ${StringArray[@]};do
	echo $val

	time cat ./tables/$val.out | ./split_simple	>  /dev/null 
done   



