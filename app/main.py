from app.factory import WebDriverFactory
from app.actuator import actuator

if __name__ == '__main__':
    driver = WebDriverFactory(config_file='config.xml').get_driver()
    actuator = actuator(driver=driver, actions_file='test_script.xml')
    actuator.exec()
