# !/bin/sh
source /etc/profile
yesterday=`date -d '-1 days' +"%Y-%m-%d"`
convert_yesterday=`date -d '-1 days' +"%Y%m%d"`

DA_mysql_prefix="mysql -N -hsg-adserver-hasoffer.cdvvzzu6xuar.ap-southeast-1.rds.amazonaws.com -P33060 -udecipher -pdecipherpwd decipher_server"
stats_mysql_prefix="mysql -N -h sgpadservernew-slave-01.cdvvzzu6xuar.ap-southeast-1.rds.amazonaws.com -P33060 -uadservermm -pmmadserver adserver_report_0605"

workdir=/home/fhf/monitor/
tmpdir=$workdir"tmp/"
da_stats_File=$tmpdir$yesterday"_da_stats.log"
da_convent_File=$tmpdir$yesterday"_da_convent.log"
da_stats_resultFile=$tmpdir$yesterday"_all_result.data"
#查询DA统计数据输出到文件
echo "
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
-- 点击下发
(select stats_day,appid,count(click_id) send_click_count from offer_stats where stats_day = '$yesterday' group by appid) send_click on basic.appid=send_click.appid
left join 
-- 点击上报
(select appid,count(click_time) upload_click_count from offer_stats where stats_day = '$yesterday' and click_time is not null group by appid) upload_click on basic.appid=upload_click.appid
left join 
-- 上报成功点击
(select appid,click_response_code,count(click_response_code) upload_click_success from offer_stats where stats_day = '$yesterday' and click_response_code in (100,101) and click_time is not null and click_response_code is not null group by appid) click_success on basic.appid=click_success.appid
left join
-- sbdjsb
(select appid,click_response_code,count(click_response_code) upload_click_faild from offer_stats where stats_day = '$yesterday' and click_response_code not in (100,101) and click_time is not null and click_response_code is not null group by appid) click_faild on basic.appid=click_faild.appid
-- 安装下发
left join
(select appid,count(install_send_time) install_send_count from offer_stats where stats_day = '$yesterday' and install_send_time is not null group by appid) install_click on basic.appid=install_click.appid
left join
-- 安装上报
(select appid,count(install_time) install_upload_count from offer_stats where stats_day = '$yesterday' and install_time is not null group by appid) install_upload on basic.appid=install_upload.appid
left join
-- 上报成功安装
(select appid,count(install_response_code) insall_upload_success from offer_stats where stats_day = '$yesterday' and install_time is not null and install_response_code is not null and install_response_code <>106 group by appid) install_success on basic.appid=install_success.appid
" | eval $DA_mysql_prefix | sort -k1 > $da_stats_File

#查询AdServer中DA中配置的app的转化数据
echo "
SELECT appid, SUM(conv) FROM hour_past_7day ad inner join ad_offer_pkg pkg on ad.offerid=pkg.id WHERE day='$convert_yesterday' and placementid in (484) group by appid,day;
" | eval $stats_mysql_prefix | sort -k1 > $da_convent_File

#将两个查询结果进行合并
join -a1 $da_stats_File $da_convent_File > $da_stats_resultFile

#调用发送邮件接口
sh $workdir"send_report_daily.sh"
