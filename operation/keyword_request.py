#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
from common.Log import log
from common.set_title import getrootdirectory
from common.yaml_util1 import read_yaml, write_yaml, load_ini
from operation.ResultBase import ResultBase
from operation.all_requests import new_requests

data_file_path = os.path.join(getrootdirectory(), "config", "setting.ini")
api_root_url = load_ini(data_file_path)["host"]["api_root_url"]

def keyword_request(name,method,url,data):
    """
    获取所有结果
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    method = method
    url = api_root_url + url
    data = data
    name = name
    if read_yaml() == None:
        header = None
    else:
        header = read_yaml()
    re = new_requests.all_send_requests(method=method,url=url,data=data,headers=header)
    result.success = False
    if re.json()['code'] == 200:
        result.success = True
        # log.info(result.success)
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(re.json()["code"], re.json()["data"])
    if 'token' in re.text:
        token_values = {'token': re.json()['data']['result']['token']}
        write_yaml(token_values, yaml_file='/extract_token.yaml')
    # result.data = re.json()["data"]['result']['username']
    result.data = re.text
    # result.json = re.text
    log.info("resulr.data数据为:{}".format(result.success))
    result.response = re
    log.info("{} ==>> 返回状态码为 >> {}".format(name,result.response.status_code))
    return result
