from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, browser='chrome'):
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser ,You can enter 'ff' or 'chrome'." % browser)

    def findElement(self, element):
        """
        :param element:元素传参格式(indentifier type, value)；e.g  ('id', 'username')查找id=username的元素
        :return:elem 查找到的与元素对象
        """
        try:
            type = element[0]
            value = element[1]
            if type == 'id':
                elem = self.driver.find_element_by_id(value)

            elif type == 'name':
                elem = self.driver.find_element_by_name(value)

            elif type == 'class':
                elem = self.driver.find_element_by_class_name(value)

            elif type == 'link_text':
                elem = self.driver.find_element_by_link_text(value)

            elif type == 'xpath':
                elem = self.driver.find_element_by_xpath(value)

            elif type == 'css':
                elem = self.driver.find_element_by_css_selector(value)

            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    def findElements(self, element):

        try:
            type = element[0]
            value = element[1]
            if type == 'id':
                elem = self.driver.find_elements_by_id(value)

            elif type == 'name':
                elem = self.driver.find_elements_by_name(value)

            elif type == 'class':
                elem = self.driver.find_elements_by_class_name(value)

            elif type == 'link_text':
                elem = self.driver.find_elements_by_link_text(value)

            elif type == 'css':
                elem = self.driver.find_elements_by_css_selector(value)

            elif type == 'xpath':
                elem = self.driver.find_elements_by_xpath(value)

            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    def open(self, url):
        if url != '':
            self.driver.get(url)
        else:
            raise ValueError("url不正确")

    def sendKeys(self, element, text):
        # 操作输入框
        element.send_keys(text)

    def enter(self, element):
        # 回车
        element.send_keys(Keys.RETURN)

    def click(self, element):
        # 点击
        element.click()

    def quit(self):
        self.driver.quit()

    def getAttribute(self, element, attribute):
        # 返回元素属性
        return element.get_attribute(attribute)

    def getText(self, element):
        # 返回元素text
        return element.text

    def getTitle(self):
        # 返回窗口title
        return self.driver.title

    def getCurrentUrl(self):
        # 返回当前url
        return self.driver.current_url

    def getScreenshot(self, targetpath):
        # 截图并保存到路径targetpath
        self.driver.get_screenshot_as_file(targetpath)

    def maximizeWindow(self):
        # 最大化窗口
        self.driver.maximize_window()

    def back(self):
        # 上一页
        self.driver.back()

    def forward(self):
        # 下一页
        self.driver.forward()

    def getWindowSize(self):
        # 获取当前窗口宽、高
        return self.driver.get_window_size()

    def refresh(self):
        # 刷新当前页
        self.driver.refresh()
        self.driver.switch_to()
