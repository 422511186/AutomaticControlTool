import time


def click(driver, selector):
    element = driver.find_element_by_css_selector(selector)
    element.click()


def input_text(driver, data):
    selector, text = data.split(',')
    element = driver.find_element_by_css_selector(selector)
    element.clear()
    element.send_keys(text)


def wait(driver, seconds):
    time.sleep(seconds)
