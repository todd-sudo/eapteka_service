import random
import time
from typing import Optional

from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from parser.conf_selenium import get_web_driver
from exceptions import ParceException
from parser.get_proxy import get_proxy_list


def parse_object(driver: webdriver.Firefox) -> Optional[tuple]:
    try:
        main_div = driver.find_element(By.CLASS_NAME, "new-offer-box")
    except NoSuchElementException as e:
        return None
    try:
        name = main_div.find_element(By.TAG_NAME, "h1")
        name = name.text.strip()
    except NoSuchElementException:
        name = ""
    try:
        card_info = main_div.find_element(By.CLASS_NAME, "offer-card__info")
    except NoSuchElementException:
        return None
    try:
        ps = card_info.find_elements(By.TAG_NAME, "p")
    except NoSuchElementException:
        return None
    brand = ""
    for p in ps:
        if "роизводитель" in p.text.strip():
            _brand = p.find_element(By.TAG_NAME, "a").text.strip()
            if _brand != "":
                brand = _brand
    try:
        price_old = card_info.find_element(
            By.CLASS_NAME, "offer-tools__old-price"
        )
        price_old = int(price_old.text.strip().replace(" ", ""))
    except NoSuchElementException:
        price_old = 0
    try:
        price = card_info.find_element(
            By.CLASS_NAME, "offer-tools__price_num-strong"
        )
        price = int(price.text.strip().replace(" ", ""))
    except NoSuchElementException:
        price = 0
    is_active = True
    if price == 0:
        is_active = False
    return name, brand, price, price_old, is_active


proxy_list = get_proxy_list()


def get_products_e_apteka(
        sku: str,
        city_name: str,
        category: str,
) -> Optional[tuple]:

    proxy = {
        "proxy": {
            "http": random.choice(proxy_list)
        }
    }
    url = f"https://www.eapteka.ru/{city_name}/goods/id{sku.strip()}/"
    print(url)
    # url = f"https://2ip.ru/"
    driver: Firefox = get_web_driver()
    # driver.delete_all_cookies()
    # driver.implicitly_wait(60)
    driver.get(url)
    print("начинаю паузу")
    time.sleep(3)
    print(driver.page_source)
    # driver.delete_all_cookies()
    try:
        print("запускаю парсинг")
        obj = parse_object(driver)
        if obj is not None:
            name, brand, price, price_old, is_active = obj
            return sku, name, brand, price, price_old, is_active, category
    except ParceException as e:
        print(e)

    finally:
        driver.close()
        driver.quit()

    return None

