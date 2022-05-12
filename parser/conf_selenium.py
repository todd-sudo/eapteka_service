import os
from seleniumwire import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_web_driver(url: str):
    root_path = os.getcwd()

    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    options.set_preference("dom.webdriver.enabled", False)

    profile = webdriver.FirefoxProfile()

    profile.set_preference('dom.webdriver.enabled', False)
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    profile.update_preferences()

    driver = webdriver.Firefox(
        executable_path=root_path + '/geckodriver',
        options=options,
        firefox_profile=profile,
        desired_capabilities=DesiredCapabilities.FIREFOX,
        # proxy=proxy,
    )

    driver.get(url)
    return driver
