#!/bin/sh
yesterday=`date +"%Y-%m-%d" -d "-1day"`
echo $yesterday
basedir=/export/shelltest/da/
tmpdir=${basedir}tmp/
da_stats_file=${tmpdir}da_stats.log

trap "" exit

da_mysql_prefix="mysql -N -h10.200.10.149 -P3306 -uzhaofeng -p123456 decipher_server"

sql="
select  
	basic.appid,basic.offer_id,basic.cvr,basic.install,
	if(send_click.send_click_count is null,0,send_click.send_click_count) as 点击下发 ,
	if(upload_click.upload_click_count  is null,0,upload_click.upload_click_count ) 点击上报,
	if(click_success.upload_click_success  is null,0,click_success.upload_click_success) 上报点击成功,
	if(click_faild.upload_click_faild  is null,0,click_faild.upload_click_faild ) 上报点击失败,
	if(install_click.install_send_count  is null,0,install_click.install_send_count) 安装下发,
	if(install_upload.install_upload_count  is null,0,install_upload.install_upload_count) 安装上报,
	if(install_success.insall_upload_success  is null,0,install_success.insall_upload_success) 上报安装成功
	 from app_basic_info  basic
left join
-- 点击下发\n
(select stats_day,appid,count(click_id) send_click_count from offer_stats where stats_day = '$yesterday' group by appid) send_click on basic.appid=send_click.appid
left join 
-- 点击上报\n
(select appid,count(click_time) upload_click_count from offer_stats where stats_day = '$yesterday' and click_time is not null group by appid) upload_click on basic.appid=upload_click.appid
left join 
-- 上报成功点击\n
(select appid,click_response_code,count(click_response_code) upload_click_success from offer_stats where stats_day = '$yesterday' and click_response_code in (100,101) and click_time is not null and click_response_code is not null group by appid) click_success on basic.appid=click_success.appid
left join
-- sbdjsb \n
(select appid,click_response_code,count(click_response_code) upload_click_faild from offer_stats where stats_day = '$yesterday' and click_response_code not in (100,101) and click_time is not null and click_response_code is not null group by appid) click_faild on basic.appid=click_faild.appid
-- 安装下发\n
left join
(select appid,count(install_send_time) install_send_count from offer_stats where stats_day = '$yesterday' and install_send_time is not null group by appid) install_click on basic.appid=install_click.appid
left join
-- 安装上报\n
(select appid,count(install_time) install_upload_count from offer_stats where stats_day = '$yesterday' and install_time is not null group by appid) install_upload on basic.appid=install_upload.appid
left join
-- 上报成功安装\n
(select appid,count(install_response_code) insall_upload_success from offer_stats where stats_day = '$yesterday' and install_time is not null and install_response_code is not null and install_response_code <>106 group by appid) install_success on basic.appid=install_success.appid
"

echo -e $sql |eval $da_mysql_prefix > $da_stats_file
