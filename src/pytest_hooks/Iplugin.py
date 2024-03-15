from typing import List

import pytest
import os
import requests
from _pytest.config import Config, hookspec
from _pytest.main import Session
# data={}
#
# @pytest.hookimpl(hookwrappwer = True)
# def pytest_pyfunc_call(func):
#
#
# 	outcome = yield

# def pytest_configure():
# 	print("之前测试用例开始执行")
#
# def pytest_unconfigure():
# 	print("之后测试案例执行")
#
# def pytest_sessionfinish():
# 	print("所有session结束后执行这段代码逻辑")
from _pytest.nodes import Item
from _pytest.reports import TestReport
from datetime import datetime

total_cases = 0
skiped_cases = 0
passed_cases = 0
failed_cases = 0
start_times = {}
end_times = {}

def pytest_collection_modifyitems(session:Session,config:Config,items:List["Item"]):
	global total_cases
	total_cases = len( items )

def pytest_runtest_setup(item:Item):
	start_times[item.nodeid] = datetime.now()

def pytest_runtest_logreport(report: TestReport):
	global skiped_cases,passed_cases,failed_cases

	if report.when == "call":
		if report.passed:
			passed_cases +=1
		elif report.failed:
			failed_cases +=1
		elif report.skipped:
			skiped_cases +=1

	end_times[report.nodeid] = datetime.now()
	duration = (datetime.now()-start_times[report.nodeid])*1000
	print(f"{report.nodeid}案例执行开始时间：{start_times[report.nodeid]}；结束时间{end_times[report.nodeid]}；执行耗时{duration}")
def pytest_sessionfinish(session:Session):
	success_rate = passed_cases / total_cases if total_cases > 0 else 0
	failure_rate = failed_cases / total_cases if total_cases > 0 else 0
	coverage_rate = (passed_cases + failed_cases) / total_cases if total_cases > 0 else 0
	print(f"案例执行完毕：成功率{success_rate}\n失败率{failure_rate}\n覆盖率{coverage_rate}")