from selenium import webdriver

from tools.browsers import AppBrowsers


def initialize_driver(browser: AppBrowsers):
    if browser == AppBrowsers.CHROMIUM:
        driver = webdriver.Chrome()
    elif browser == AppBrowsers.FIREFOX:
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")
    driver.maximize_window()
    yield driver
    driver.quit()
