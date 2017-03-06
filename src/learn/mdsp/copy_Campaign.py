# coding=UTF-8
'''
Created on 2017年3月6日

@author: Administrator
'''

import MySQLdb
import requests

# dbhosts='10.200.10.146'
# dbpassword='altamob@123'
# dbname='dsp_test_v1'
# dbuser='zhouyan'
# dbport=3306
dbhosts='10.200.10.149'
dbuser='zhaofeng'
dbpassword='123456'
dbname='dsp_test_dev'
dbport=3306

# dspHost='rtb.altamob.com/mdsp'
dspHost='http://localhost:8080/mdsp-bidder'

 
conn = MySQLdb.connect(host=dbhosts, user=dbuser, passwd=dbpassword, db=dbname, port=dbport)


def copyCampaigns(srcCampaignId,targetGroupId):
    try:
        cur = conn.cursor()
        cur.execute('select max(id) from Campaigns;')
        maxCampaignId = int(cur.fetchone()[0])
        cur.execute('select max(id) from Creatives;')
        targetCreativeId = cur.fetchone()[0]
        cur.execute('select Account.Id from Groups inner join Brands on Groups.brandId=Brands.Id and Groups.id=%s inner join Account on Account.id=Brands.accountId ;' % (targetGroupId))
        targetAccountId = cur.fetchone()[0]
        targetCampaignId=maxCampaignId+1
    #     print targetCampaignId,targetCreativeId
        
        sql='''
        insert into Campaigns(GroupID,Title,Domain,UpdatedTime,Status,DailyBudget,BudgetType) 
            select $targetGroupId,Title,Domain,UpdatedTime,Status,DailyBudget,BudgetType from Campaigns where id=$srcCampaignId;'''
        sql= sql.replace('$targetGroupId', str(targetGroupId)).replace('$srcCampaignId', str(srcCampaignId)).replace('$targetCampaignId', str(targetCampaignId));
        print sql
        print cur.execute(sql)
        sql='insert into DeviceMake(Make,Model,CampaignId) select Make,Model,$targetCampaignId from DeviceMake where campaignId=$srcCampaignId;'
        sql= sql.replace('$targetGroupId', str(targetGroupId)).replace('$srcCampaignId', str(srcCampaignId)).replace('$targetCampaignId', str(targetCampaignId));
        print sql
        print cur.execute(sql)
        sql='insert into DeviceOS(OS,OSV,CampaignID) select OS,OSV,$targetCampaignId from DeviceOS where campaignId=$srcCampaignId;'
        sql= sql.replace('$targetGroupId', str(targetGroupId)).replace('$srcCampaignId', str(srcCampaignId)).replace('$targetCampaignId', str(targetCampaignId));
        print sql
        print  cur.execute(sql)
        sql='insert into Geos(City,Region,Country,CampaignID) select City,Region,Country,$targetCampaignId from Geos where campaignId=$srcCampaignId;'
        sql= sql.replace('$targetGroupId', str(targetGroupId)).replace('$srcCampaignId', str(srcCampaignId)).replace('$targetCampaignId', str(targetCampaignId));
        print sql
        print cur.execute(sql)
        sql='insert into ConfigItems(TableName,LinkID,`Key`,`Value`,Seq) select "Campaigns",$targetCampaignId,`Key`,`Value`,Seq from ConfigItems  where tableName="Campaigns" and linkId=$srcCampaignId;'
        sql= sql.replace('$targetGroupId', str(targetGroupId)).replace('$srcCampaignId', str(srcCampaignId)).replace('$targetCampaignId', str(targetCampaignId));
        print sql
        print cur.execute(sql)
        
        #curl to dsp
        loadCampaignBudgetUrl= '{{host}}/console/loadCampaignBudget.do?cid=%s&accountId=%s'.replace('{{host}}', dspHost) % (targetCampaignId,targetAccountId)
        sendRequest(loadCampaignBudgetUrl)
        conn.commit()
#         begin copy creatives of campaigns
        copyCreatives(srcCampaignId, targetCampaignId)
        
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    finally:
        conn.close()
    

def copyCreatives(srcCampaignID,targetCampaignId):
    try:
        getMaxCreativeId = "select max(id) from Creatives;"
        cur = conn.cursor()
        cur.execute(getMaxCreativeId)
        maxIdStr=cur.fetchone()
        maxCreativeId=int(maxIdStr[0])
        
        count = cur.execute('select CampaignID,`Name`,BidPrice,AdType,AdMarkup,`Status`,ID from Creatives where campaignId=%d;' % (int(srcCampaignID)) )
        print '==' * 10
        if count>0:
            cur.scroll(0, mode='absolute')
            results = cur.fetchall()
            for r in results:
                Name=str(r[1])
                Bidprice=r[2]
                AdTpye=r[3]
                AdMarkUp=r[4]
                status=r[5]
                creativeId=r[6]
                maxCreativeId+=1
                insertCreativessql="insert into Creatives(ID,CampaignID,`Name`,BidPrice,AdType,AdMarkup,`Status`) values(%d,%s,'%s',%s,'%s','%s',%s)" % (maxCreativeId,targetCampaignId,Name,Bidprice,AdTpye,AdMarkUp,status)
                print insertCreativessql
                cur.execute(insertCreativessql)
                #insert into banner
                getBannerSql="select FileName,Path,Size,Url from Banner where creativeId=%d; " % (creativeId)
                cur.execute(getBannerSql)
                banner = cur.fetchone()
                fn=banner[0]
                p=banner[1]
                s=banner[2]
                u=banner[3]
                insertbanner="insert into Banner(CreativeId,FileName,Path,Size,Url,UpdateTime) values(%s,'%s','%s','%s','%s',CURRENT_TIMESTAMP)" % (maxCreativeId,fn, p, s, u)
                print insertbanner
                cur.execute(insertbanner)
                # insert into   ConfigItems
                getConfigSql = "select `key`,`value`,seq from ConfigItems where tableName='Creatives' and  linkId=%d; " % (creativeId)
                cur.execute(getConfigSql)
                for config in  cur.fetchall():
                    key = config[0]
                    value = config[1]
                    seq = config[2]
                    insertConfigSql = "insert into ConfigItems(TableName,LinkID,`Key`,`Value`,Seq) values('Creatives','%s','%s','%s','%s')" % (maxCreativeId,key,value,seq)
                    print insertConfigSql
                    cur.execute(insertConfigSql)
                
                sendMessage2Dsp(maxCreativeId)
            conn.commit()
            cur.close()
        else:
            print "no content!"
        print '==' * 10
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def sendMessage2Dsp(targetCreativeId):
    updateConfigUrl='{{host}}/console/updateConfig.do?creativeIds=%s'.replace('{{host}}', dspHost) % (targetCreativeId)
    sendRequest(updateConfigUrl)
    
    resetDynamicBidUrl='{{host}}/console/resetWinRateConfig.do?cid=%s'.replace('{{host}}', dspHost) % (targetCreativeId)
    sendRequest(resetDynamicBidUrl)
   
def sendRequest(requestUrl):
    response= requests.request("GET", requestUrl)
    if response.status_code != 200:
        print 'response error:',requestUrl,response.text.strip()
    else:
        print 'success:',requestUrl
    

if __name__ == '__main__':
    print 'please input target GroupId:'
    targetGroupId=raw_input()
    print 'please input src Campaignid:'
    srcCampaignId=raw_input()
    print 'copy campaignID:%s to Group:%s' % (srcCampaignId,targetGroupId)
    copyCampaigns(srcCampaignId, targetGroupId)
    


    