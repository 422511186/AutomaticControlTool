import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xml.etree.ElementTree as ET


class Client:

    def __init__(self, config_file):
        self.driver = None
        self.config = ET.parse('conf/' + config_file).getroot()
        self.driver_path = self.config.find('driver_path').text
        self.browser_type = self.config.find('browser_type').text
        self.headless = self.config.find('headless').text
        print(self.headless)
        self.default_wait_time = int(self.config.find('default_wait_time').text)

    def init_driver(self):
        if self.browser_type == 'chrome':
            options = Options()
            if self.headless == 'True':
                options.add_argument('--headless')
            self.driver = webdriver.Chrome(self.driver_path, options=options)
        elif self.browser_type == 'firefox':
            options = webdriver.FirefoxOptions()
            if self.headless == 'True':
                options.headless = True
            self.driver = webdriver.Firefox(executable_path=self.driver_path, options=options)
        else:
            print('Unsupported browser type:', self.browser_type)
            exit(1)
        self.driver.implicitly_wait(self.default_wait_time)

    def execute(self, test_file):
        test_tree = ET.parse('action/' + test_file)
        test_root = test_tree.getroot()
        for action in test_root.findall('action'):
            action_type = action.find('type').text
            action_data = action.find('data').text.split(',')
            if action_type == 'open':
                self.driver.get(action_data[0])
            elif action_type == 'input':
                self.driver.find_element_by_css_selector(action_data[0]).send_keys(action_data[1])
            elif action_type == 'click':
                self.driver.find_element_by_css_selector(action_data[0]).click()
            elif action_type == 'wait':
                time.sleep(int(action_data[0]))

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    # 使用示例
    test = Client('config.xml')
    test.init_driver()
    test.execute('test_script.xml')
    test.quit()
