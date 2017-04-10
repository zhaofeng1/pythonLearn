# -*- coding:utf-8 -*-
#Desc：DA 安装、点击、点击上报、安装上报、留存上报 流程测试代码（V1.4）
#Date：2017.1.19
#Author：zhou

import requests,logging.config,unittest,datetime,time
from pub_conf import *
from decipher.Public_Params import url_dict_arg


robotIds=[]
# robotIds=['test_fGWldkPDwd5YDX5oED5B', 'test_fGWldkPDwd5YDX5oED5B', 'test_fGWldkPDwd5YDX5oED5B', 'test_CaBsvEVO3fbpoj63oc02', 'test_CaBsvEVO3fbpoj63oc02', 'test_CaBsvEVO3fbpoj63oc02', 'test_a5s8YItD11m91IwPI0Cc', 'test_a5s8YItD11m91IwPI0Cc', 'test_a5s8YItD11m91IwPI0Cc', 'test_WDH1Yd8a0eVvHQ7PuFoj', 'test_WDH1Yd8a0eVvHQ7PuFoj', 'test_WDH1Yd8a0eVvHQ7PuFoj', 'test_3ydBRbnHH0C03BeeYX8G', 'test_3ydBRbnHH0C03BeeYX8G', 'test_3ydBRbnHH0C03BeeYX8G']
tasksAll=[]  #请求到的点击任务
task_dic={}     #请求到的点击任务，以robot为key的map
installUploads=[]  #已安装上报的任务
clkUpload_task=[] #点击上报成功的任务
clk_domain='pixel.admobclick.com'
replace_url='52.74.138.132'
#offer_ids=['7713745','29793437']
offer_ids=['46366671','29608005']

#android refer/track url/final url
android_tracking_urls = {
   offer_ids[0]: "https://app.appsflyer.com/com.mentormate.android.inboxdollars?pid=appia_int&c=NonIncent&clickid=APPIA148093303188564934422683648&af_siteid=7868&android_id=&advertising_id=bafba407-f07e-41b2-a4b6-1878f82c4a15"
    , offer_ids[1]: "http://adjust.track/xxx"}

android_refer_urls = {
    offer_ids[0]: "af_tranid%3DQuoRen75VZIdc07Rx0YjUw%26pid%3Dappia_int%26c%3DNonIncent%26clickid%3DAPPIA148093303188564934422683648%26af_siteid%3D7868%26advertising_id%3Dbafba407-f07e-41b2-a4b6-1878f82c4a15",
    offer_ids[1]: "reftag=cI451rP6Nr6o4&referrer=adjust_reftag%3DcI451rP6Nr6o4%26utm_source%3Dalchemy%26utm_campaign"}

android_final_urls_market={offer_ids[0]:"market://details?id=com.monet.boost.max&referrer=af_tranid%3DLOqx7u7wXrnRI0qNsmdPDA%26pid%3Dalchemy_int%26af_click_lookback%3D1d%26c%3Dda_yace%26af_siteid%3D30189%26clickid%3D1394010230101135601484710676329%26af_sub5%3D20000_1394010230101135601484710676329_US_2246727_0.1_416"
           }
android_final_urls_gp={offer_ids[0]:"http://play.google.com",offer_ids[1]:"http://play.google.com"}
android_final_urls_intent={offer_ids[0]:"intent://details?play.google.com",offer_ids[1]:"intent://details?play.google.com"}

#ios (ios单子无refer)/trackurl/final url
ios_tracking_urls={"20015826":"https://ad.apsalar.com/api/v1/ad?re=0&a=atomtickets_prod&i=org.gamatech.Movie-Friends&ca=Display+%28iOS%29&an=Opera+Response&p=iOS&pl=Display&udid=E819A4D1288E3938D5911131770708D5&udi5=E819A4D1288E3938D5911131770708D5&idfa=&udi1=E819A4D1288E3938D5911131770708D5&ifa1=&transid=16489556751&googleadid=&s=3480&h=97c473ea72d3b4c3686cc7612155dae75e104ca6"}
ios_refer_urls = {"20015826":""}
ios_final_urls_itms={"20015826":"itms-appss://itunes.apple.com/app/id926058555?mt=8"}
ios_final_urls_ituns={"20015826":"http://itunes.apple.com/app/id926058555?mt=8"}

#参数配置
plat='android'
#Heads={"X-Forwarded-For":conf.get('ip','US')}
Heads={"X-Forwarded-For":conf.get('ip','ID')}
ok_version='1.3'
ok_appName='com.smule.singandroid'


class reqTasks(unittest.TestCase):
    local_path = os.path.join(os.path.dirname(__file__))
    logging.config.fileConfig(os.path.join(local_path, "../logging.conf"))
    logger = logging.getLogger(__name__)


    #获取留存任务表中可用的留存任务
    # def getRetainIds(self):
    #     with decipher_db().cursor() as cursor:
    #         sql = '''select * from retain_task_info where data_type='0' '''
    #         cursor.execute(sql)
    #         result=cursor.fetchall()
    #         return result


    #获取点击任务
    def est01_getClickTasks(self):
        robot=random_str()
        # robot='test_ke0snVbbspDP8xaiGKQk'
        req_header=Heads
        body=getdecipher_taskDataSendParams(str(robot))
        print 'body:',body
        body['platform']=plat
        body['sdk_version']=ok_version
        body['app_name']=ok_appName
        bodys=json.dumps(body).replace('"',"'")
        params=encrypt(bodys)   #调用加密函数加密body参数
        print params
#         req=requests.post(getdecipher_taskDataSend(),headers=req_header,data=params)   #发起任务请求
#         if req.status_code==200:
#             tasks = json.loads(dencrypt(req.content))  #解密返回的任务
#             self.logger.info("请求任务接口状态：%s robot %s"% (req.status_code,robot))
#             if tasks['clickdata']:     #提取下发的click任务
#                 self.logger.info("请求到的点击任务：%s"%tasks['clickdata'])
#                 global tasksAll
#                 tasksAll=tasks['clickdata']
#                 task_dic[robot]=tasksAll
#                 # robotIds.append(robot)
#             else:
#                 self.logger.info("Error:clickdata为空:%s"%tasks)
#         elif req.status_code==204:
#             print "Err:没有可用单子",req.status_code
#         else:
#             print "Err:请求失败：",req.status_code,req.text,robot,req.url,req_header,params


    #模拟302跳转
    def est02_url302(self):
        if tasksAll:
            count=0
            for clk in tasksAll:
                count+=1
                clickU = clk['click']
                Reurl=clickU.replace(clk_domain,replace_url)
                response = requests.head(Reurl, headers=click_headers_ua)
                location_url = response.headers['Location']
                if "error" in location_url:
                    self.logger.info("点击服务异常，未跳出Altamob:%s" %Reurl)
                else:
                    self.logger.info("android-302跳转:%s %s"%(count,location_url))
                    while response.status_code == 302:
                        count=count+1
                        if location_url.startswith("http://") or location_url.startswith("https://"):
                            response = requests.head(location_url, headers=click_headers_ua)
                            self.logger.info("err:%s",response.status_code)
                            if response.status_code!=302:
                                break
                            else:
                                location_url = response.headers['Location']
                                self.logger.info("302跳转:%s %s"%(count,location_url))
                        else:
                            break

    #点击上报
    def est03_clickUpload(self):
        # time.sleep(180)
        if task_dic:
            for x in task_dic.keys():
                req_header=Heads
                for clktask in task_dic[x]:
                    clks=url_dict_arg(clktask['click'])
                    offer_id=clks['offer_id']
                    if offer_id in android_tracking_urls and offer_id in android_refer_urls:
                        rep_body=json.dumps(getDecipherClickUploadParams()).replace(getDecipherClickUploadParams()['robotId'],x)\
                                        .replace(getDecipherClickUploadParams()['sdk_version'],ok_version)\
                                        .replace(getDecipherClickUploadParams()['app_name'],ok_appName)\
                                        .replace(getDecipherClickUploadParams()['clickId'],clktask['dataid'])\
                                        .replace(getDecipherClickUploadParams()['clickUrl'],clktask['click'])\
                                        .replace(getDecipherClickUploadParams()['referer'],android_refer_urls[offer_id])\
                                        .replace(getDecipherClickUploadParams()['trackingUrl'],android_tracking_urls[offer_id])\
                                        .replace(getDecipherClickUploadParams()['finalUrl'],android_final_urls_gp[offer_id])
                        body_clk=rep_body.replace('"',"'")#转换标准json格式，双引号替换为单引号
                        params_clkupload=encrypt(body_clk)   #调用加密函数加密body参数
                        req=requests.post(getdecipher_click_upload(),headers=req_header,data=params_clkupload)   #clk上报
                        if req.status_code==200 and req.content=='success':
                            clkUpload_task.append(body_clk)       #点击上报数据提取备用
                            self.logger.info("Right:点击上报成功:robot-%s ,dataid-%s ,offerid-%s" %(x,clktask['dataid'],offer_id))
                            robotIds.append(x)
                        else:
                            self.logger.info("Error:点击上报失败:%s %s %s" %(req.status_code,req.content,body_clk))

    #安装上报
    def est04_installUpload(self):
        # print robotIds
        count=0
        for robotflag in robotIds:
            count+=1
            req_header=Heads
            body=getdecipher_taskDataSendParams(str(robotflag))
            body['platform']=plat
            body['sdk_version']=ok_version
            body['app_name']=ok_appName
            bodys=json.dumps(body).replace('"',"'")
            params=encrypt(bodys)   #调用加密函数加密body参数
            req=requests.post(getdecipher_taskDataSend(),headers=req_header,data=params)   #发起任务请求
            if req.status_code==200:
                print count
                tasks = json.loads(dencrypt(req.content))  #解密返回的任务
                self.logger.info("请求任务接口状态：%s"% req.status_code)
                if tasks['trackdata']:     #获取安装任务
                    self.logger.info("拿到安装任务详情：%s"% tasks['trackdata'])
                    for track in tasks['trackdata']:
                        if track['dataType']=='install':
                            if getInstalledInfos():
                                for info in getInstalledInfos():    #若设备未安装过app,则执行安装
                                    if unicode(robotflag) !=unicode(info['robot_id']) or unicode(track['app_name'])!=unicode(info['appid']):
                                        req_header=Heads
                                        rep_body=json.dumps(getDecipherInstallUploadParams()).\
                                                    replace(getDecipherInstallUploadParams()['clickId'],track['dataid']).\
                                                    replace(getDecipherInstallUploadParams()['sdk_version'],ok_version).\
                                                    replace(getDecipherInstallUploadParams()['app_name'],ok_appName)
                                        body_clk=rep_body.replace('"',"'")#转换标准json格式，双引号替换为单引号
                                        params_installUpload=encrypt(body_clk)   #调用加密函数加密body参数
                                        req=requests.post(getdecipher_install_upload(),headers=req_header,data=params_installUpload)   #安装上报
                                        if req.status_code==200 and req.content=='success':
                                            installUploads.append(body_clk)       #安装上报数据提取备用
                                            self.logger.info("Right:安装上报成功 %s"%track['dataid'])
                                        else:
                                            self.logger.info("Error:安装上报失败,状态码%s,dataid:%s"%(req.status_code,track['dataid']))
                                    break
                            else:
                                # req_header=Heads
                                rep_body=json.dumps(getDecipherInstallUploadParams()).\
                                            replace(getDecipherInstallUploadParams()['clickId'],track['dataid']).\
                                            replace(getDecipherInstallUploadParams()['sdk_version'],ok_version).\
                                            replace(getDecipherInstallUploadParams()['app_name'],ok_appName)
                                body_clk=rep_body.replace('"',"'")#转换标准json格式，双引号替换为单引号
                                params_installUpload=encrypt(body_clk)   #调用加密函数加密body参数
                                req=requests.post(getdecipher_install_upload(),headers=req_header,data=params_installUpload)   #安装上报
                                if req.status_code==200 and req.content=='success':
                                    installUploads.append(body_clk)       #安装上报数据提取备用
                                    self.logger.info("Right:安装上报成功1，dataid:%s"%track['dataid'])
                                else:
                                    self.logger.info("Error:安装上报失败1,状态码：%s,dataid：%s"%(req.status_code,track['dataid']))
            else:
                self.logger.info("安装步骤-请求任务接口状态：%s ,dataid：%s"% (req.status_code,robotflag))

            #（单个设备请求流程）每次走完请求 点击 安装上报流程后，将字典、列表内存清空，避免数据重复，造成重复请求和上报
            #如果批量上报，请注释掉以下2行
            # robotIds[:]=[]
            # task_dic.clear()

    #循环发起请求和点击上报
    def test005_range(self):
        for x in range(500):
            if x==1:
                break
            else:
                print '\n',x
                reqTasks.est01_getClickTasks(self)
                # reqTasks.est02_url302(self)
                reqTasks.est03_clickUpload(self)
                #每上报1次点击，清空字典，避免数据累加，重复上报
                task_dic.clear()

        #执行安装上报，延迟60s+进行安装上报
        time.sleep(90)
        reqTasks.est04_installUpload(self)
        #将发起请求的robot保存到本地文件
        nowtime=datetime.datetime.now()
        fileObj=open('E:/logs/robots.txt','a')
        fileObj.write('\n'+(str(nowtime))+'\n'+ (str(robotIds)))
        print str(robotIds)

    #执行留存上报
    def est006_retainUpload(self):
        count=0
        for robotflag in robotIds:
            count+=1
            req_header=Heads
            body=getdecipher_taskDataSendParams(str(robotflag))
            body['sdk_version']=ok_version
            body['app_name']=ok_appName
            bodys=json.dumps(body).replace('"',"'")
            params=encrypt(bodys)   #调用加密函数加密body参数
            req=requests.post(getdecipher_taskDataSend(),headers=req_header,data=params)   #发起任务请求
            if req.status_code==200:
                tasks = json.loads(dencrypt(req.content))  #解密返回的任务
                self.logger.info("请求任务接口状态：%s"% req.status_code)
                if tasks['trackdata']:
                    for track in tasks['trackdata']:
                        if track['dataType']=='retain':
                            self.logger.info("拿到留存任务详情：%s-- %s" % (count,tasks['trackdata']))
                            req_header=Heads
                            rep_body=json.dumps(getDecipherRetainUploadParams())\
                                            .replace(getDecipherRetainUploadParams()['clickId'],track['dataid'])\
                                            .replace(getDecipherRetainUploadParams()['sdk_version'],ok_version)\
                                            .replace(getDecipherRetainUploadParams()['app_name'],ok_appName)
                            body_clk=rep_body.replace('"',"'")#转换标准json格式，双引号替换为单引号
                            params_retainUpload=encrypt(body_clk)   #调用加密函数加密body参数
                            req=requests.post(getdecipher_retain_upload(),headers=req_header,data=params_retainUpload)   #留存上报
                            if req.status_code==200:
                                print "Right:留存上报成功",req.content,track['dataid']
                            else:
                                print "Error:留存上报失败",req.status_code,req.content,track['dataid']
            else:
                self.logger.info("请求任务接口状态：%s"% req.status_code)


#执行函数
if __name__=='__main__':
    unittest.main()
    #关闭数据库连接
    decipher_db().close()
    sql_conn()[0].close()