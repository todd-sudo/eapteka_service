import os

from seleniumwire import webdriver as webd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_web_driver(proxy=None):
    root_path = os.getcwd()
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.set_preference("dom.webdriver.enabled", False)

    profile = webd.FirefoxProfile()
    profile.set_preference('dom.webdriver.enabled', False)
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", "193.36.58.158")
    profile.set_preference("network.proxy.http_port", "8000")
    profile.set_preference("network.proxy.username", "QPYXyF")
    profile.set_preference("network.proxy.password", "rGurC6")
    # profile.update_preferences()

    driver = webdriver.Firefox(
        executable_path=root_path + '/geckodriver',
        options=options,
        firefox_profile=profile,
        # seleniumwire_options=proxy,
        desired_capabilities=DesiredCapabilities.FIREFOX,
        # proxy=proxy,
    )
    driver.set_page_load_timeout(3600 * 2 * 2)
    return driver
