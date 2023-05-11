from src.actuator.actuator import actuator
from src.factory.driver_factory import WebDriverFactory

if __name__ == '__main__':
    driver = WebDriverFactory(config_file='config.xml').get_driver()
    actuator = actuator(driver=driver, actions_file='test_script.xml')
    actuator.exec()
    driver.quit()
