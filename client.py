import os
import time

import grpc

import eapteka_pb2
import eapteka_pb2_grpc


def get_data():
    name = "abakan"

    with grpc.insecure_channel("141.101.188.7:8088", options=(("grpc.enable_http_proxy", 0),)) as ch:
        stub = eapteka_pb2_grpc.RunParserStub(ch)
        response = stub.run_parser(eapteka_pb2.City(name=name))
        print(response)
    # except KeyboardInterrupt:
        # ch.unsubscribe(close)
        # exit()
        ch.close()


def close(ch):
    ch.close()


if __name__ == '__main__':
    get_data()
