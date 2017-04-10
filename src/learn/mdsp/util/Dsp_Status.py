# coding=utf-8
'''
Created on 2017年3月7日

@author: Administrator
'''
from learn.mdsp.util.WebChatUtils import WebChatUtils
from learn.mdsp.util.MysqlUtil import Mysql
import time
from time import sleep

def sendWebChat(user,message):
    chatUtil = WebChatUtils()
    chatUtil.sendMessage(user, message)

if __name__ == '__main__':
    
    BIDALL = -1
    BIDWIN = -1
    while True:
        print "BIDALL:%d;BIDWIN:%d;" % (BIDALL,BIDWIN)
        day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        print day
        hour = time.strftime('%H',time.localtime(time.time())) 
        print hour
        sqlUtil = Mysql()
        
        sql = '''SELECT sum(Bidall)Bidall,sum(Bidwin)Bidwin
                  FROM Report_Stream WHERE Date = %s and Hour = %s
            '''
        param = []
        param.append(day)
        param.append(hour)
        #获取统计
        result = sqlUtil.getOne(sql, param)
        print result
        tempbidall = result["Bidall"]
        tempbidwin = result["Bidwin"]
        
        if tempbidall is None:
            tempbidall = 0
        if tempbidwin is None:
            tempbidwin = 0
        
        print "tempbidall:%d;tempbidwin:%d;" % (tempbidall,tempbidwin)
        
        strList = []        
        if tempbidall == BIDALL:
            strList.append("Bidall")
        if tempbidwin == BIDWIN:
            strList.append("Bidwin")
            
        BIDALL = tempbidall
        BIDWIN = tempbidwin
        
        
        column = ""
        message = ""
        if len(strList)>0:
            for s in strList:
                column += s+","
            column = column[0:len(column)-1]
            message = "以下列："+column+"在5分钟内无变化!"
        if message != "":
            print message
            
        sleep(3)
    
