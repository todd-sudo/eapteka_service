import os
from base64 import b64encode

from seleniumwire import webdriver as webd
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_web_driver(proxy=None):
    root_path = os.getcwd()
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
    profile.set_preference('network.proxy.socks', "212.3.105.11")
    profile.set_preference('network.proxy.socks_port', "4145")
    # profile.set_preference('signon.autologin.proxy', 'true')
    # profile.set_preference('network.proxy.share_proxy_settings', 'false')
    # profile.set_preference('network.automatic-ntlm-auth.allow-proxies', 'false')
    # profile.set_preference('network.auth.use-sspi', 'false')

    # proxy_data = {'address': '212.3.105.11:4145'}
    # proxy_dict = {'proxyType': ProxyType.MANUAL,
    #               'httpProxy': proxy_data['address'],
    #               'ftpProxy': proxy_data['address'],
    #               'sslProxy': proxy_data['address'],
    #               'noProxy': '',
    #               'socksUsername': proxy_data['username'],
    #               'socksPassword': proxy_data['password']}
    #
    # proxy_config = Proxy(proxy_dict)
    # print(proxy_config)
    # profile.set_preference("network.proxy.type", 1)
    # profile.set_preference("network.proxy.http", "193.36.58.158")
    # profile.set_preference("network.proxy.http_port", 8000)
    # profile.set_preference("network.proxy.username", "QPYXyF")
    # profile.set_preference("network.proxy.password", "rGurC6")
    # profile.set_preference("network.proxy.no_proxies_on", "localhost, 127.0.0.1")
    profile.update_preferences()

    driver = webdriver.Firefox(
        executable_path=root_path + '/geckodriver',
        options=options,
        firefox_profile=profile,
        # seleniumwire_options=proxy,
        desired_capabilities=DesiredCapabilities.FIREFOX,
        proxy=proxy_config,
    )
    driver.set_page_load_timeout(3600 * 2 * 2)
    return driver
