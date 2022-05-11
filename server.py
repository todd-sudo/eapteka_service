import threading
import time
from concurrent import futures

import grpc

import eapteka_pb2
import eapteka_pb2_grpc
from parser.parser import get_products_e_apteka


def parse_data(sku: str, city_name: str, category: str):
    return get_products_e_apteka(
        sku=sku, city_name=city_name, category=category
    )


class RunParserEapteka(eapteka_pb2_grpc.RunParserServicer):
    def run_parser(self, request, context):
        obj = parse_data(
            sku=request.sku,
            city_name=request.city_name,
            category=request.category,
        )
        if obj is not None:
            sku, name, brand, price, price_old, category = obj
            return eapteka_pb2.Product(
                name=name,
                sku=sku,
                brand=brand,
                price=price,
                price_old=price_old,
                category=category
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    eapteka_pb2_grpc.add_RunParserServicer_to_server(RunParserEapteka(), server)
    server.add_insecure_port("[::]:8088")
    server.start()
    try:
        while True:
            print(
                f"Server started: 127.0.0.1:8088\n"
                f"Threads {threading.active_count()}"
            )
            time.sleep(10)
    except KeyboardInterrupt as e:
        server.stop(0)


if __name__ == '__main__':
    serve()
