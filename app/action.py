import time
from abc import abstractmethod
from xml.etree.ElementTree import Element

from selenium.webdriver.android.webdriver import WebDriver


class action:
    _type: str

    @abstractmethod
    def execute(self, driver: WebDriver):
        pass


class open_action(action):
    url: str

    def __init__(self, data: Element):
        self._type = 'open_action'
        self.url = data.find('url').text

    def execute(self, driver: WebDriver):
        driver.get(url=self.url)


class input_action(action):
    css_selector: str
    text: str

    def __init__(self, data: Element):
        self._type = 'input_action'
        self.css_selector = data.find('css_selector').text
        self.text = data.find('text').text

    def execute(self, driver: WebDriver):
        driver.find_element_by_css_selector(self.css_selector).send_keys(self.text)


class click_action(action):
    css_selector: str

    def __init__(self, data: Element):
        self._type = 'click_action'
        self.css_selector = data.find('css_selector').text

    def execute(self, driver: WebDriver):
        driver.find_element_by_css_selector(self.css_selector).click()


class wait_action(action):
    secs: int

    def __init__(self, data: Element):
        self._type = 'wait_action'
        self.secs = int(data.find('secs').text)

    def execute(self, driver: WebDriver):
        time.sleep(self.secs)


class quit_action(action):

    def __init__(self):
        self._type = 'quit_action'

    def execute(self, driver: WebDriver):
        driver.quit()
