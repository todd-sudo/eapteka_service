import os
from base64 import b64encode

from seleniumwire import webdriver as webd
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_web_driver(proxy=None):
    root_path = os.getcwd()
    options = webd.FirefoxOptions()
    options.add_argument("--headless")
    options.set_preference("dom.webdriver.enabled", False)

    profile = webd.FirefoxProfile()
    profile.set_preference('dom.webdriver.enabled', False)
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    driver = webd.Firefox(
        executable_path=root_path + '/geckodriver',
        options=options,
        firefox_profile=profile,
        seleniumwire_options=proxy,
        desired_capabilities=DesiredCapabilities.FIREFOX,
        # proxy=proxy_config,
    )
    driver.set_page_load_timeout(3600 * 2 * 2)
    return driver
