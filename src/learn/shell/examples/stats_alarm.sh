#!/bin/sh
work_dir=/export/shelltest/
tmp_dir=${work_dir}tmp/

sql_result=${tmp_dir}sql_result.txt

function alarm(){
	#查询统计数据
	mysql_local="mysql -N -h10.200.10.149 -P3306 -uzhaofeng -p123456 dsp_test_dev"
	#sql="select count(1) from Campaigns "
	#echo $sql
	#count=$(echo $sql | eval $mysql_local)
	#echo $count
	sql="select ID,Title from Campaigns "
	echo $sql
	
	
	
	
	
	
	#result=$(echo $sql | eval $mysql_local)
	#echo $result
	#echo $result > $sql_result
	#cat $sql_result |awk '{print }'
}

alarm