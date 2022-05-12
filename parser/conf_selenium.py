import os
from base64 import b64encode

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_web_driver(proxy=None):
    root_path = os.getcwd()
    h = "193.36.58.208:8000"
    login = "QPYXyF"
    p = "rGurC6"
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = h
    proxy.socks_proxy = h
    proxy.ssl_proxy = h
    proxy.socksUsername = login
    proxy.socksPassword = p
    capabilities = DesiredCapabilities.FIREFOX
    proxy.add_to_capabilities(capabilities)

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.set_preference("dom.webdriver.enabled", False)

    profile = webdriver.FirefoxProfile()
    profile.set_preference('dom.webdriver.enabled', False)
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    driver = webdriver.Firefox(
        executable_path=root_path + '/geckodriver',
        options=options,
        firefox_profile=profile,
        desired_capabilities=capabilities,
        proxy=proxy,
    )
    driver.set_page_load_timeout(3600 * 2 * 2)
    return driver
