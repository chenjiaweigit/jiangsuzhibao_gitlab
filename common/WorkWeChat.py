#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import re
import time

import requests

from common.Send_Email import locathost_ip
from common.set_title import getrootdirectory
from common.yaml_util1 import load_ini



data_file_path = os.path.join(getrootdirectory(),'config','setting.ini')
work_wechat = load_ini(data_file_path)["work_wechat"]
corpid = work_wechat['corpid']
corpsecret = work_wechat['corpsecret']
token_url = work_wechat['token_url']
url = work_wechat['url']

def workwhat_access_token():

    params = {
        "corpid" : corpid,
        "corpsecret" : corpsecret
    }
    access_token = requests.get(token_url,params=params)
    # print(re.findall('access_token":"(.+?)"',access_token1)[0])
    return access_token.json()['access_token']

def send_workwhat(message):

    now_time = time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())
    data = {
        "touser": "@all",
        "msgtype": "textcard",
        "agentid": 1000002,
        "textcard": {
            "title" : "自动化监控报告",
            "description" : "<div class=\"gray\">"+now_time+"</div> <div class=\"normal\">"+message+"</div><div class=\"highlight\">可登录jenkins查看报告详情</div>",
            "url" : locathost_ip,
            "btntxt":"更多"
        },
        "safe": 0
    }
    new_url = url+'?access_token='+workwhat_access_token()
    send_message = requests.post(url=new_url,json=data)
    print(send_message.json())

