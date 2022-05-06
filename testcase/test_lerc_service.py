#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import allure
import pytest
from common.Log import log
from operation.keyword_request import keyword_request
from testcase.conftest import api_data

class Test_lerc_service:
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_08'])
    def test_08(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_09'])
    def test_09(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_10'])
    def test_10(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_11'])
    def test_11(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_12'])
    def test_12(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_13'])
    def test_13(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_14'])
    def test_14(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_15'])
    def test_15(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_16'])
    def test_16(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("{name}-预期成功")
    @pytest.mark.smoke1
    # @pytest.mark.run(order=8)
    @pytest.mark.parametrize("module,name,method,url,data,except_pt,except_code,except_result", api_data['test_17'])
    def test_17(self, module, name, method, url, data, except_pt, except_code, except_result):
        allure.dynamic.feature("{}模块".format(module))
        allure.dynamic.story("用例--/{}/--预期成功".format(name))
        allure.dynamic.description("该用例是针对 监控{name}功能是否正常 场景的测试")
        log.info("*************** {}-开始执行用例 ***************".format(name))
        result = keyword_request(name=name, method=method, url=url, data=data)
        log.info("状态码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.status_code))
        assert result.success == except_pt, log.info("断言失败：{}".format(result.error))
        assert result.response.status_code == except_code, log.info("断言失败，except_code返回为：{}".format(except_code))
        log.info("except_result数据为：{}".format(except_result))
        assert result.data != "", log.info("断言失败：data数据返回为空>>{}".format(result.data))
        log.info("*************** {}-结束执行用例 ***************".format(name))