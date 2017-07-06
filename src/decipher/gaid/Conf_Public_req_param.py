# -*- coding:utf-8 -*-
# Desc：SDK4.0接口 公共方法
# Date：2016.11.4
# Author：zhou

import sys
from decipher.Public_Params import *
sys.path.append('../')


# url请求路径
API_PATH = conf.get("ads4", "API_PATH")
# redis_host = conf.get("redis", "host")
# redis_port = conf.get("redis", "port")
token = conf.get("ads4", "token")
pid1='1662684189370000_1769833153868157'




# 定义请求参数
def getParams():
    return {
    "placement_id": "1662684189370000_1769833153868147",
    "count": 5,
    "app_pkg": "com.niutest.com",
    "app_version": "2.1.6",
    "aid": "a2849f901c3210ca",
    "gaid": "000-111-222-333",
    "imei": "12597845663221",
    "os_version": "5.2",
    "sdk_version": "3.4.4.4101",
    "user_agent": "Mozilla/5.0 (Linux; Android 4.4.2; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
    "language": "en",
    "country": "US",
    "network_type": "1"
}


def get_click_upload():
    return "http://" + API_HOSTS + conf.get("sdk_click_report", "API_PATH")

def get_install_report():
    return "http://" + API_HOSTS + conf.get("sdk_install", "API_PATH")


# 定义拼装url方式
def getTestApiPath():
    return 'http://' + API_HOSTS + API_PATH



def sql_statement():
    sql = '''select DISTINCT ssc.subsite,i.content_rating_val,t.code,d.lang,d.title,d.description,o.*,i.*
                from feed_offers o
                LEFT JOIN feed_offer_target t ON t.offer_id = o.id
                LEFT JOIN feed_offer_description d ON d.app_info_id=o.app_info_id
                LEFT JOIN feed_app_info i ON i.id=o.app_info_id
			    LEFT JOIN subsite_source_config ssc ON ssc.source=o.source
                WHERE 1=1
                AND t.code = '%s'
                AND t.status = 'active'
                AND i.status ='published'
                AND o.platform = 'android'
                AND d.lang = '%s'
                AND o.status IN ('published','active')
                AND ssc.subsite=%s
                AND o.id in (%s)'''
    # AND (o.sync_time>FROM_UNIXTIME(UNIX_TIMESTAMP(now())-60*60*24*20) or o.sync_time is null)'''
    return sql
