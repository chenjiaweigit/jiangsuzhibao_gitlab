#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import allure
import pytest
from common.Log import log
from operation.keyword_request import keyword_request
from testcase.conftest import api_data

# @allure.step("步骤1 ==>> 登录用户")
# def step_1(data):
#     log.info("步骤1 ==>> 登录用户：{}".format(data))
a = 1
class Test_screen:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    @pytest.mark.run(order=2)
    @pytest.mark.skipif(a==0,reason='因为a=1所以不执行')
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_02'])
    def test_screen_01(self,module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")

        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name,method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get('data',{}).get('code')))
        assert result.success == except_pt,log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code,log.info("断言失败，except_code返回为：{}".format(except_code))
        # log.info(f'{json.dumps(result.response.json(), sort_keys=True, indent=2)}')
        log.info("except_result数据为：{}".format(except_result))
        assert str(except_result) in result.data
        assert  result.data != "","数据返回为空"
        assert  result.response.json()['data']['apcp']['50~65'] != "","小麦apcp数据返回为空"
        assert  result.response.json()['data']['rh']['66~68%'] != "","小麦rh数据返回为空"
        assert  result.response.json()['data']['ssrd']['660~675'] != "","小麦ssrd数据返回为空"
        assert  result.response.json()['data']['tave']['＞18'] != "","小麦tave数据返回为空"
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    @pytest.mark.run(order=3)
    # @pytest.mark.skip(reason="暂时不执行该用例")
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_03'])
    def test_screen_02(self,module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")

        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get('data',{}).get('code')))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        # log.info(f'{json.dumps(result.response.json(), sort_keys=True, indent=2)}')
        log.info("except_result数据为：{}".format(except_result))
        assert str(except_result) in result.data,log.info("断言失败：{}".format(except_result))
        assert result.data != "",log.info("断言失败：数据返回为空>>{}".format(result.data))
        assert result.response.json()['data']['apcp']['120~140'] != "", "apcp数据返回为空"
        assert result.response.json()['data']['rh']['77~78%'] != "", "rh数据返回为空"
        assert result.response.json()['data']['ssrd']['700~715'] != "", "ssrd数据返回为空"
        assert result.response.json()['data']['tave']['＞26'] != "", "tave数据返回为空"
        log.info("*************** {}-结束执行用例 ***************".format(name))

if __name__ == '__main__':
    pytest.main(['-v','-s',"test_screen.py"])