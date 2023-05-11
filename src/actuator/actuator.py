import xml.etree.ElementTree as ET

from src.factory.action_factory import action_factory
from selenium.webdriver.android.webdriver import WebDriver


class actuator:
    data: map
    actions: list

    def __init__(self, driver: WebDriver, actions_file: str = None):
        self.driver = driver
        self.parse(actions_file=actions_file)

    def parse(self, actions_file: str = None):
        test_tree = ET.parse(source='../resource/action/' + actions_file)
        test_root = test_tree.getroot()
        self.actions = test_root.findall(path='action')

    def exec(self):
        for action in self.actions:
            action_factory.get_action(action).execute(driver=self.driver)
