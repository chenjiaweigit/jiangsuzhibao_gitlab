#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import allure
import pytest

from common.Log import log
from operation.keyword_request import keyword_request
from testcase.conftest import api_data


class Test_recovery_play:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_04'])
    def test_04(self, module, name, method, url, data, except_pt, except_code, except_result):
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
        assert str(except_result) in result.data, log.info("断言失败：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        result.data1 = eval(result.data)
        assert result.data1["data"]["mean"] != "",log.info("断言失败：mean数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_05'])
    def test_05(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")

        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info(
            "状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get('data', {}).get('code')))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        # log.info(f'{json.dumps(result.response.json(), sort_keys=True, indent=2)}')
        log.info("except_result数据为：{}".format(except_result))
        assert str(except_result) in result.data, log.info("断言失败：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        # assert result.data["mean"] != "", log.info("断言失败：mean数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_06'])
    def test_06(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")

        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info(
            "状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get('data', {}).get('code')))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        # log.info(f'{json.dumps(result.response.json(), sort_keys=True, indent=2)}')
        log.info("except_result数据为：{}".format(except_result))
        assert str(except_result) in result.data, log.info("断言失败：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        # assert result.data["mean"] != "", log.info("断言失败：mean数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_07'])
    def test_07(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")

        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info(
            "状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get('data', {}).get('code')))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        # log.info(f'{json.dumps(result.response.json(), sort_keys=True, indent=2)}')
        log.info("except_result数据为：{}".format(except_result))
        assert str(except_result) in result.data, log.info("断言失败：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        # assert result.data["mean"] != "", log.info("断言失败：mean数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))