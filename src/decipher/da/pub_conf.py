# -*- coding:utf-8 -*-
#Desc：
#Date：
#Author：zhou

import sys,json
from random import Random
import os
from decipher.Public_Params import sql_conn
import ConfigParser
sys.path.append("../")
import pymysql
from Public_Params import *


reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
#sys.setdefaultencoding('utf-8')

# 获取当前脚本文件所在目录的完整路径
local_path = os.path.join(os.path.dirname(__file__))
conf = ConfigParser.ConfigParser()
#读取配置文件 url请求路径
conf.read(os.path.join(local_path, "../config.txt"))
API_HOSTS = conf.get('api_host', 'API_HOSTS_DA')
API_PATH = conf.get("decipher_taskDataSend", "API_PATH")
# clickurl跳转相关配置
click_headers_ua ={"User-Agent":conf.get("click_url", "click_ua")}
clk_domain='pixel.admobclick.com'
clk = conf.get("click_url", "clk")
replace_url = conf.get("api_host", "replace_url")
secretKey = conf.get("click_url", "secretKey")

def urlStr_args(url):
    url_url_dict = {}
    for url_arg in url.split("&"):
        k, v = url_arg.split("=")
        url_url_dict[k] = v
    return url_url_dict


#获取已安装app设备列表
def getInstalledInfos():
    with decipher_db().cursor() as cursor:
        sql = '''SELECT * from install_task_info'''
        cursor.execute(sql)
        result=cursor.fetchall()
        return result

#获取下发offer所属的app
def getHasofferApps(offerid):
    with sql_conn()[0].cursor() as cursor:
        sql=''' SELECT * FROM feed_offers WHERE id = %s '''
        sql = sql % offerid
        cursor.execute(sql)
        result=cursor.fetchall()
        return result

#获取留存任务表中可用的留存任务
def getRetainIds():
    with decipher_db().cursor() as cursor:
        sql = '''select * from retain_task_info where data_type='0' '''
        cursor.execute(sql)
        result=cursor.fetchall()
        return result


# 任务请求url
def getdecipher_taskDataSend():
    return "http://" + API_HOSTS + API_PATH

#任务请求接口参数
def getdecipher_taskDataSendParams(devices):
    return{
        "platform": "android",
        "app_version": "10",
        "sdk_version": "3.1",
        "aid": devices,
        "app_name": "niubobo.test"}


#点击上报接口url
def getdecipher_click_upload():
    return "http://" + API_HOSTS + conf.get("decipher_click_upload", "API_PATH")

#点击上报接口参数
def getDecipherClickUploadParams():
    return {
            "robotId":"aabbcc",
            "clickId":"ncbtest1480403720584",
            "clickUrl":"http://com.test",
            "referer":"http://test.referer",
            "trackingUrl":"http://test.tackingurl",
            "clickResult":"1",
            "platform": "android",
            "app_version": "10",
            "sdk_version": "3.1",
            "app_name": "niubobo.test",
            "finalUrl":"market://"
            }





#安装上报接口url
def getdecipher_install_upload():
    return "http://" + API_HOSTS + conf.get("decipher_install_upload", "API_PATH")

#安装上报参数
def getDecipherInstallUploadParams():
    return {
            "platform": "android",
            "installResult": "200",
            "app_version": "10",
            "sdk_version": "3.1",
            "clickId": "100011020010224151482995102215",
            "app_name": "niubobo.test",
            "info": ""
        }


#留存上报接口
def getdecipher_retain_upload():
    return "http://" + API_HOSTS + conf.get("decipher_retain_upload", "API_PATH")

#留存上报参数
def getDecipherRetainUploadParams():
    return {
            "platform": "android",
            "survivalResult": "1",
            "app_version": "10",
            "sdk_version": "3.1",
            "clickId": "100011020010224151482995102215",
            "app_name": "niubobo.test",
            "info": ""
        }



#调用客户端加密jar包加密post body参数
def encrypt(body):
    os.chdir(local_path)
    cmd = "java -jar encrypt.jar  0 \"" + body + "\""
    os.system(cmd)
    result = ''
    with open('./result.txt') as file:
        for line in file.readlines():
            result += line.strip()
    return result


#解密api返回任务数据
def dencrypt(body):
    os.chdir(local_path)
    cmd = 'java -jar encrypt.jar  1 \"' + body.replace('\n','')+"\""
    os.system(cmd)
    result=''
    with open('result.txt') as file:
        for line in file.readlines():
            result += line.strip()
    return result


#DA数据库连接
def decipher_db():
    # data_base="db_decipher"
    data_base='db_decipher_line'
    db_host = conf.get(data_base, 'db_host')
    db_user_name = conf.get(data_base, 'db_user_name')
    db_passwd = conf.get(data_base, 'db_passwd')
    db_name = conf.get(data_base, 'db_name1')
    db_port = int(conf.get(data_base, 'db_port1'))
    connection1 = pymysql.connect(host=db_host,
                                  user=db_user_name,
                                  password=db_passwd,
                                  db=db_name,
                                  port=db_port,
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
    return  connection1


def random_str(randomlength=20):
    strings = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        strings+=chars[random.randint(0, length)]
    return 'test_'+strings

if __name__ == "__main__":
    decipher_db()
    param={"platform": "android","app_version": "10","sdk_version": "3.0","aid": 'zqCGiAGCv1wrcSq50DmG4NchqoL1ks',"app_name": "niu.test"}
    body=json.dumps(param).replace('"', "'")
    print body
#     cl='test0113be4e9b31bda3'
#     obj=open('E:\logs\ll.txt','a')
#     obj.write(encrypt(body))
#     print encrypt(cl)

