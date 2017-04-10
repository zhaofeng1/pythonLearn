# coding=utf-8
'''
Created on 2017年3月6日

@author: Administrator
'''
import requests
import json
from os.path import sys
class WebChatUtils:
    
    def __init__(self):
        # 微信企业号的appid dsp使用
        self.corpid_dsp = "wxf601632127c9d62b";
        #微信企业号的corpSecret dsp使用
        self.corsecret_dsp = "sgBNXtGvG6LkzZFdNCHvkCpM7oKOOMYPc4zsbOIlqpTdEacl9hHeVzbtW3gUgpZf";
        #agentid dsp alert
        self.agentid_dsp = "3";
        #获取token接口
        self.web_chat_access_token_api_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + self.corpid_dsp + "&corpsecret=" + self.corsecret_dsp;
        #发送信息接口
        self.web_chat_send_message_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=";
    
#     @staticmethod
    def sendMessage(self,user,message):
        #先获取token
        print self.web_chat_access_token_api_url
        r = requests.get(self.web_chat_access_token_api_url,timeout=30)
        if r.status_code == 200:
            tokenJson = r.json()
            print tokenJson

        if tokenJson != "":
            token = tokenJson["access_token"]
            print token
        #发送信息
        url = self.web_chat_send_message_url + token
        params = {}
        msg = {}
        msg["content"] = "test"
        params["msgtype"] = "text"
        params["safe"] = "0"
        params["text"] = msg
        params["touser"] = user
        params["agentid"] = self.agentid_dsp
        
        data = json.dumps(params)
        
        print data
        
        r = requests.post(url, data)
        print r.text
        
         
if __name__ == '__main__':
    touser = sys.argv[1]
    context = sys.argv[2]
    chatUtil = WebChatUtils()
    chatUtil.sendMessage("zhaofeng", "测试")



