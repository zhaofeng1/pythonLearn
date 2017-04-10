# -*- coding:utf-8 -*-
import pymysql.cursors
import urlparse,os
import ConfigParser

#读取配置文件
local_path = os.path.join(os.path.dirname(__file__))
conf = ConfigParser.ConfigParser()
conf.read(os.path.join(local_path, "./config.txt"))


# url请求路径主域名
API_HOSTS=conf.get('api_host','API_HOSTS')

#clickurl跳转相关配置
click_headers=conf.get("click_url","click_ua")

# clk="10.200.10.224:8090"
clk=conf.get("click_url","clk")
clk_pixel=conf.get('click_url','clk_pixel')
clk_webeye=conf.get('click_url','clk_webeye')
replace_url=conf.get("api_host","replace_url")
secretKey=conf.get("click_url","secretKey")

filename='E:\s2s-download\s2s\json_new.txt'


#分隔url
def url_dict_arg(url):
    url_url_dict = {}
    for url_arg in url.split("?")[1].split("&"):
        k, v = url_arg.split("=")
        url_url_dict[k] = v
    return url_url_dict


def str_dict_arg(url):
    url_url_dict = {}
    for url_arg in url.split(',"'):
        # print url
        k, v = url_arg.split(':',1)
        url_url_dict[k.strip('{').strip('"')] = v.strip('"')
    return url_url_dict

def url_dict_args(url1,url2):
    url_url1_dict = {}
    url_url2_dict={}
    for url_arg1 in url1.split("&"):
        k, v = url_arg1.split("=")
        url_url1_dict[k] = v
    for url_arg2 in url2.split("&"):
        k, v = url_arg2.split("=")
        url_url2_dict[k] = v
    return url_url1_dict,url_url2_dict


#分隔location
def location_dict_arg(url):
    if '\\a' in url:
        url = url.replace('\\a', '=')
        url = url.replace('\\b', '&')
    if '\a' in url:
        url = url.replace('\a', '=')
        url = url.replace('\b', '&')
    if "%253D" in url:
        url=url.replace("%253D","=")
    if "%2526" in url:
        url=url.replace("%2526","&")
    if 'p1=subsite' in url:
        url = url.replace("p1=subsite", "")
        url = url.replace("p3=parameter", "")
    if '&p1=' in url:
        url = url.replace("&p1=", "&tid=")
        url = url.replace("&p2=", "&sub_id=")
    if "%3D" in url:
        url = url.replace('%3D', '=')
    if "%26" in url:
        url = url.replace("%26", "&")
    if "=p1=" in url:
        url=url.replace("=p1=","=para&p1=")
    if "=type=" in url:
        url=url.replace("=type=","=para&type=")
    if "=p=" in url:
        url=url.replace("=p=","=para&p=")
    if "%5Cb"  in url:
        url=url.replace("%5Cb","&")
    if "%5Ca" in url:
        url=url.replace("%5Ca","=")
    if  "%7B"in url:
        url=url.replace("%7B","{")
        url=url.replace("%7D","}")
    if "%25" in url:
        url=url.replace("%25","%")
    if "%3a" in url:
        url=url.replace("%3a",":")
    if "%2f" in url:
        url=url.replace("%2f","/")
    query = urlparse.urlparse(url).query
    url = dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])
    return url


#数据库连接
def sql_conn():
    # 数据库连接配置读取
    data_base = "db"
    db_host_hasoffer = conf.get(data_base, 'db_host_hasoffer')
    db_host_report = conf.get(data_base, 'db_host_report')
    db_user_name = conf.get(data_base, 'db_user_name')
    db_passwd = conf.get(data_base, 'db_passwd')
    db_name1 = conf.get(data_base, 'db_name1')
    db_port1 = int(conf.get(data_base, 'db_port1'))
    db_name2 = conf.get(data_base, 'db_name2')
    db_port2 = int(conf.get(data_base, 'db_port2'))

    connection1 = pymysql.connect(host=db_host_hasoffer,
                                  user=db_user_name,
                                  password=db_passwd,
                                  db=db_name1,
                                  port=db_port1,
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
    connection2 = pymysql.connect(host=db_host_report,
                                  user=db_user_name,
                                  password=db_passwd,
                                  db=db_name2,
                                  port=db_port2,
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
    return connection1, connection2

#code&lang
def geo_langs():
    return {'US':'en',
	 'ID':'id',
	 'TH':'th',
	 'IN':'en',
	 # 'CA':'fr',
	 # 'GB':'en',
	 'BR':'pt',
	 'MX':'es',
	 # 'ES':'es',
	 'VN':'vi',
	 'PH':'en',
	 'MY':'ms',
	 # 'KR':'ko',
	 # 'JP':'ja',
	 # 'DE':'de',
	 'RU':'tt',
	 # 'IT':'it',
	 # 'TR':'tr',
	 # 'PL':'pl',
	 # 'FR':'fr'
                 }

#语言&ip
def ip_lang():
    return {
        conf.get('ip','US'):'en',
        conf.get('ip','ID'):'id',
        conf.get('ip','TH'):'th',
        conf.get('ip','IN'):'en',
        conf.get('ip','BR'):'pt',
        conf.get('ip','MX'):'es',
        conf.get('ip','VN'):'vi',
        conf.get('ip','PH'):'en',
        conf.get('ip','MY'):'ms',
        conf.get('ip','RU'):'tt'
    }

#ip&code
def ip_geo():
    return {
        conf.get('ip','US'):'US',
        conf.get('ip','ID'):'ID',
        conf.get('ip','TH'):'TH',
        conf.get('ip','IN'):'IN',
        conf.get('ip','BR'):'BR',
        conf.get('ip','MX'):'MX',
        conf.get('ip','VN'):'VN',
        conf.get('ip','PH'):'PH',
        conf.get('ip','MY'):'MY',
        conf.get('ip','RU'):'RU'
    }


'''模拟器:对应国家的模拟地址'''
def simulator():
    return  { 'US':conf.get("UrlValidator","US"),
     'ID':conf.get("UrlValidator","ID"),
     'TH':conf.get("UrlValidator","TH"),
     'IN':conf.get("UrlValidator","IN"),
     'CA':conf.get("UrlValidator","CA"),
     'GB':conf.get("UrlValidator","GB"),
     'BR':conf.get("UrlValidator","BR"),
     'MX':conf.get("UrlValidator","MX"),
     'ES':conf.get("UrlValidator","ES"),
     'VN':conf.get("UrlValidator","VN"),
     'PH':conf.get("UrlValidator","PH"),
     'MY':conf.get("UrlValidator","MY"),
     'KR':conf.get("UrlValidator","KR"),
     'JP':conf.get("UrlValidator","JP"),
     'DE':conf.get("UrlValidator","DE"),
     'RU':conf.get("UrlValidator","RU"),
     'IT':conf.get("UrlValidator","IT"),
     'TR':conf.get("UrlValidator","TR"),
     'PL':conf.get("UrlValidator","PL"),
     'FR':conf.get("UrlValidator","FR")}


#sql hasoffer
def sql_hasoffer():
    hasoffer_sql='''select DISTINCT t.code,ssc.subsite,i.category,i.min_os_version,i.cover_url,i.logo,i.filesize,i.appstore_url,d.lang,d.title,d.description,o.*
                FROM feed_offers o
                LEFT JOIN feed_offer_target t on t.offer_id = o.id
                LEFT JOIN feed_offer_description d ON d.app_info_id=o.app_info_id
                LEFT JOIN feed_app_info i ON i.id=o.app_info_id
                LEFT JOIN subsite_source_config ssc on ssc.source=o.source
                left join ok_source_config osc on osc.source_code = ssc.source
                WHERE 1=1
                AND t.status = 'active'
                AND o.status IN ('published','active')
                AND i.status = 'published'
                and osc.`status`='published'
                AND t.code = '%s'
                AND ssc.subsite=%s
                AND o.platform = '%s'
                GROUP BY t.code,o.id'''
    return hasoffer_sql


#sql report
def sql_rep():
    report_sql='''select ap.subsite_id,pkg.source,app.placement,cp.offerid,cp.country,pkg.app_info_id,sum(cp.click) as click,ROUND(sum(cp.conv)/sum(cp.click),5) AS cvr,sum(cp.impression) as impression,
                sum(cp.conv) as conv,ROUND(sum(cp.revenue)/sum(cp.impression)*1000.0,5) as ecpm,ROUND(sum(cp.revenue)/sum(cp.click)*1000.0,5) as ecpc,sum(cp.revenue) as revenue,
                ROUND(sum(cp.click)/sum(cp.impression),5) as ctr  from ad_offer_stats_hour_algorithm cp
                inner join ad_app_placement app on app.id=cp.placementid
                inner join ad_app ap on ap.id=app.app_id
                INNER JOIN ad_offer_pkg pkg ON pkg.id=cp.offerid
                where cp.country='%s'
                    AND ap.type='%s'
                    AND ap.subsite_id=%s
                GROUP BY cp.offerid,cp.country,pkg.app_info_id
                ORDER BY ecpc DESC '''
    return report_sql

#sql norefer
def sql_norefer():
    report_norefer_offergeo='''SELECT * from schedule_noreferrer_stat'''
    report_norefer_geo='''SELECT * from schedule_noreferrer_stat_no_country'''
    return report_norefer_offergeo,report_norefer_geo


#输出数据到文件
def writeFiles(files,txts):
    file_object=open(files,'a')
    file_object.write(txts+'\n')
    file_object.close()

#解析文件行数据
def logLocal(filename):
    texts=[]
    for text in open(filename):
        lines=text.split('\n')
        for line in lines:
            # line=urlDecode(line)
            texts.append(line)
    return texts


#s2s json数据存储为txt，读取txt数据转为dic
def txtData2dic(filename):
    list=[]
    text=logLocal(filename)
    for x in text[:-1]:
        textFormat=x.strip('[').strip(']').split("},")
        for i in textFormat:
            text2json=str_dict_arg(i)
            list.append(text2json)
    return list

