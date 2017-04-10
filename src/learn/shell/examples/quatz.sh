#!/bin/sh
log_file=/export/shelltest/log/quatz.log
for i in 1 2 3;do
	daytemp=$(date "+%Y-%m-%d %H:%M:%S")
	echo $daytemp
	
	echo "quatz for start:$daytemp" >> $log_file
	echo $i
	echo "quatz for end:" >> $log_file
done