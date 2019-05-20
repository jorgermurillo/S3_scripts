#!/bin/bash


n_fields=$1


declare -a StringArray=("100000"  "500000" "750000"  "1000000" "2000000")



for val in ${StringArray[@]};do
	echo $val

	python S3_write_table.py  "./tables/$val.out"  $val 
	python S3_write_table.py  "./tables/$val.out2"  $val".2" 	
	
	printf "\n\n"
done
