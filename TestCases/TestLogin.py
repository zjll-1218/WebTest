# coding=utf-8
import unittest
import time
from Common import CommonConfiguration, LogUtils
from Pages.LoginPage import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.base_url = CommonConfiguration.baseUrl()
        LogUtils.createLog("test_login")

    def test_1(self):
        """
        正确用户名、密码：
        1.选择机构‘test999’
        2.输入用户‘test’
        3.输入密码‘123456’
        """

        LogUtils.Log("open url %s" % self.base_url)
        page = LoginPage()
        page.open(self.base_url)
        page.selectOrg('test999')
        page.setUsername('test')
        page.setPassport('123456')
        page.clickLogin()

        time.sleep(3)
        title = page.getTitle()
        self.assertEqual(title, '田田网1')
        page.quit()

    def test_2(self):
        """
        正确用户名、密码：
        1.选择机构‘test999’
        2.输入用户‘test’
        3.输入密码‘123456’
        """

        LogUtils.Log("open url %s" % self.base_url)
        page = LoginPage()
        page.open(self.base_url)
        page.selectOrg('test999')
        page.setUsername('test')
        page.setPassport('123456')
        page.clickLogin()

        time.sleep(3)
        title = page.getTitle()
        self.assertEqual(title, '田田网')
        page.quit()


if __name__ == '__main__':
    unittest.main()
