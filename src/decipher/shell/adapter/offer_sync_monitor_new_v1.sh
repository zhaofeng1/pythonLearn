#!/bin/sh
#offer同步数据监控
#29 * * * * sh /export/fhf/monitor/offer_sync_monitor_new.sh

source /etc/profile
#sources=(10030 10020 10010 10040 10090  10150 10160 10170 10210 10070 10250  10230 10260 10330 10080  10320 10350 10340 10280 10390 10180 10012 10410 10022 10400 10152 10162 10172 10182)   

#mysqlInfo="mysql hasoffer_0720 -hsg-adserver-hasoffer.cdvvzzu6xuar.ap-southeast-1.rds.amazonaws.com -P33060 -uzhoujian -pzhoujian*jd23F3"
mysqlInfo="mysql hasoffer_0805 10.200.10.149 -P33060 -uzhaofeng -p123456"


function initSources(){
  #sourceConfig=`$mysqlInfo -N -e "select group_concat(source_code)  from ok_source_config where status='published';"`
  sourceConfig=`$mysqlInfo -N -e "SET SESSION group_concat_max_len = 102400; select  replace(group_concat(source_code,'|',source_name),' ','_') from ok_source_config where status='published';"`
  echo -e $sourceConfig
}




function checkSyncData()
{
  s=$1
  n=$2
  lastSyncTime=`$mysqlInfo -N -e "select max(sync_time) from feed_offers where source=$s  limit 1;"`
  echo "$lastSyncTime $s"
  ts=`date -d "$lastSyncTime" +%s`
  now=`date +%s`
  tsDiff=$[now-ts];
  echo $lastSyncTime $s $n
	active_count=`$mysqlInfo -N -e "select count(id) from feed_offers where source=$s and status = 'active' limit 1"`
	echo "$active_count $s" 
  if [ $tsDiff -gt 5400 ];then
    echo $lastSyncTime
    echo $tsDiff
    f='【预警主题】：上游api同步服务故障\\n【预警时间】：%s \\n【预警详情】： 上游 %s(%s) 的Offer超%d分钟没更新\\n 【active】active num:%d\\n'
    now=`date "+%Y-%m-%d %H:%M:%S"`
    minute=`expr $tsDiff / 60`
    msg="`printf "$f" "$now" "$n" "$s" "${minute}" "${active_count}"`"
    #curl -d "{\"name\":\"wushuaifei|yangbaojie|zhaofeng|dupengcheng|songjingpin|wanghanyu|lichen\",\"content\":\"$msg\"}" 'http://52.74.138.132/wxtoken/v1/send'
    #curl 'http://52.74.138.132/wxtoken/v1/ring_dpc'
  fi


}
sources=$(echo -e `initSources`)

OLDIFS=$IFS
IFS=","
sc=$(echo $sources)
IFS=$OLDIFS

#echo $sources
#echo $OLDIFS
for source in  ${sc[@]}
do
 #echo $source
 arr=(${source//|/ });
 s=${arr[0]} ;
 n="${arr[1]}"
 if [ $s -ge 20000 ];then
    continue;
 fi
 checkSyncData "$s" "$n"
done