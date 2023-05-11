import time
from abc import abstractmethod

from selenium.webdriver.android.webdriver import WebDriver


class action:
    _type: str

    @abstractmethod
    def execute(self, driver: WebDriver):
        pass


class open_action(action):
    url: str

    def __init__(self, url: str):
        self._type = 'open_action'
        self.url = url

    def execute(self, driver: WebDriver):
        driver.get(url=self.url)


class input_action(action):
    css_selector: str
    data: str

    def __init__(self, css_selector: str, data: str):
        self._type = 'input_action'
        self.css_selector = css_selector
        self.data = data

    def execute(self, driver: WebDriver):
        driver.find_element_by_css_selector(self.css_selector).send_keys(self.data)


class click_action(action):
    css_selector: str

    def __init__(self, css_selector: str):
        self._type = 'click_action'
        self.css_selector = css_selector

    def execute(self, driver: WebDriver):
        driver.find_element_by_css_selector(self.css_selector).click()


class wait_action(action):
    secs: int

    def __init__(self, secs: int):
        self._type = 'wait_action'
        self.secs = secs

    def execute(self, driver: WebDriver):
        time.sleep(self.secs)
