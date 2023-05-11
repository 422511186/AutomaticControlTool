from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xml.etree.ElementTree as ET


class WebDriverFactory:

    def __init__(self, config_file: str = 'config.xml'):
        self.config = ET.parse('../resource/conf/' + config_file).getroot()
        self.driver_path = self.config.find('driver_path').text
        self.browser_type = self.config.find('browser_type').text
        self.headless = self.config.find('headless').text
        self.default_wait_time = int(self.config.find('default_wait_time').text)
        if self.browser_type == 'chrome':
            options = Options()
            if self.headless == 'True':
                options.add_argument('--headless')
            self.driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        elif self.browser_type == 'firefox':
            options = webdriver.FirefoxOptions()
            if self.headless == 'True':
                options.headless = True
            self.driver = webdriver.Firefox(executable_path=self.driver_path, options=options)
        else:
            print('Unsupported browser type:', self.browser_type)
            exit(1)
        self.driver.implicitly_wait(self.default_wait_time)

    def get_driver(self):
        return self.driver
