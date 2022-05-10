import threading
import time
from concurrent import futures

import grpc

import eapteka_pb2
import eapteka_pb2_grpc


def parse_data():
    return "sku 123", "name", "brand", 2323, 23123, "category"


class RunParserEapteka(eapteka_pb2_grpc.RunParserServicer):
    def run_parser(self, request, context):
        sku, name, brand, price, price_old, category = parse_data()
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
    server.add_insecure_port("127.0.0.1:8088")
    server.start()
    try:
        while True:
            print(f"server on: threads {threading.active_count()}")
            time.sleep(10)
    except KeyboardInterrupt as e:
        server.stop(0)


if __name__ == '__main__':
    serve()
