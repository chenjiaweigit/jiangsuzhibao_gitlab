#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import locale
#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
import _bootlocale
_bootlocale.getpreferredencoding = lambda do_setlocale = True : "utf-8"

import shutil
import pytest
from common.set_title import *

if __name__ == '__main__':
    pytest.main()
    shutil.copy('./config/environment.properties','./temp')
    shutil.copy('./config/categories.json', './temp')
    os.system('allure generate ./temp -o ./report --clean')
    # 自定义allure窗口标题
    set_windos_title("自动化测试报告")
    # 自定义allure测试报告标题
    report_title = get_json_data("自动化测试报告")
    write_json_data(report_title)
    # 支持本地查看allure报告
    '''
    os.system('chomd 777 doubleClickReadReport.sh')
    os.system('./doubleClickReadReport.sh') 
    '''
