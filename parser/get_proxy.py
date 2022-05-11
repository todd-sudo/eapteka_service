import json


def get_proxy_list() -> list:
    with open("parser/proxy.json", "r") as file:
        data = json.load(file)
    return data
