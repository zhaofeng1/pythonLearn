#!/bin/sh

# 微信企业号的appid dsp使用
corpid_dsp="wxf601632127c9d62b";
#微信企业号的corpSecret dsp使用
corsecret_dsp="sgBNXtGvG6LkzZFdNCHvkCpM7oKOOMYPc4zsbOIlqpTdEacl9hHeVzbtW3gUgpZf";
#agentid dsp alert
agentid_dsp="3";
#获取token接口
web_chat_access_token_api_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=$corpid_dsp&corpsecret=$corsecret_dsp";
#发送信息接口
web_chat_send_message_url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=";
    
function sendWebChat(){
	#获取token
	echo $web_chat_access_token_api_url
	token=$(curl -s "$web_chat_access_token_api_url" | jq -r .access_token)
	echo "token:$token"
	if [ -z $token ];then
		echo get token error!
		exit 101
	fi
	
	#发送信息
	msg='{'
	msg=$msg'"msgtype":"text",'
	msg=$msg'"safe":"0",'
	msg=$msg'"text":{"content":"'$2'"},'
	msg=$msg'"touser":"'$1'",'
	msg=$msg'"agentid":"3"'
	msg=$msg'}'
	
	echo $msg
	sendurl="$web_chat_send_message_url$token"
	result=$(curl -s -d $msg $sendurl)
	echo $result
	
	if [ -z $result ];then
		echo "send message error!"
		exit 102
	else
		error=$(echo $result|jq -r .errcode)
		if [ $error == 0 ];then
			errmsg=$(echo $result|jq -r .errmsg)
			echo "end msg error, with error $errcode: $errmsg"
        	exit 102
    	else
    		echo ok
    	fi
	fi
	
}

	sendWebChat zhaofeng test	