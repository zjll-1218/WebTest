# coding=utf-8
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from TestCases import TestLogin
import TestCases


test1 = TestLoader().loadTestsFromTestCase(TestCases.TestLogin.TestLogin)

suite = TestSuite([test1])

h = HTMLTestRunner(combine_reports=True, report_name="TestReport", add_timestamp=True).run(suite)
