#!/bin/sh
function sendmessage(){
	
	#$* 和 $@ 一样，只有在双引号括着的时候不一样
	echo $#
	#echo $*
	for s in "$*";do
		echo $s
	done
	#echo $@
	for s in "$@";do
		echo $s
	done
}

	sendmessage 1 2 3	