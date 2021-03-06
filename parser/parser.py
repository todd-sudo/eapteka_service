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
    return name, brand, price, price_old


proxy_list = get_proxy_list()


def get_products_e_apteka(
        sku: str,
        city_name: str,
        category: str,
) -> Optional[tuple]:
    url = f"https://www.eapteka.ru{city_name}goods/id{sku.strip()}/"
    driver: Firefox = get_web_driver()
    driver.get(url)
    time.sleep(3)

    try:
        obj = parse_object(driver)
        if obj is not None:
            name, brand, price, price_old = obj
            return sku, name, brand, price, price_old, category
    except ParceException as e:
        print(e)

    finally:
        driver.close()
        driver.quit()

    return None

