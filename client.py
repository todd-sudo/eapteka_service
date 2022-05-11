import os
import time

import grpc

import eapteka_pb2
import eapteka_pb2_grpc


PRODUCTION_HOST = "141.101.188.7"
PRODUCTION_PORT = "18088"
LOCAL_HOST = "localhost"
LOCAL_PORT = "8088"


def get_data():
    with grpc.insecure_channel(
            f"{PRODUCTION_HOST}:{PRODUCTION_PORT}",
            options=(("grpc.enable_http_proxy", 0),)
    ) as ch:
        stub = eapteka_pb2_grpc.RunParserStub(ch)
        response = stub.run_parser(
            eapteka_pb2.RequestData(
                city_name="abakan",
                sku="105320",
                category="Test"
            )
        )
        print(response.sku)
        print(response.name)
        print(response.brand)
        print(response.price)
        print(response.price_old)
        print(response.is_active)
        print(response.category)
    # except KeyboardInterrupt:
        # ch.unsubscribe(close)
        # exit()
        ch.close()


def close(ch):
    ch.close()


if __name__ == '__main__':
    get_data()
