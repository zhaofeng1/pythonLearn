#!/bin/sh
yesterday=`date +"%Y-%m-%d" -d "-1day"`
echo $yesterday
basedir=/export/shelltest/da/
tmpdir=${basedir}tmp/
da_stats_file=${tmpdir}da_stats.log

da_mysql_prefix="mysql -N -h10.200.10.149 -P3306 -uzhaofeng -p123456 decipher_server"

sql="a b c\n
d
e"

echo -e $sql
