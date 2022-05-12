from parser.parser import get_products_e_apteka


def main():
    get_products_e_apteka(
        city_name="/abakan/",
        sku="499787",
        category="Test"
    )


if __name__ == '__main__':
    main()
