import grpc
import logging

import send_data_pb2_grpc
import send_data_pb2
import queue

data_queue = queue.Queue(10)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = send_data_pb2_grpc.SendDataStub(channel)
        response = stub.SingleData(send_data_pb2.SendRequest(request_message='Send data to visualize'))
        print('Client Received: ', response.queues)


if __name__ == '__main__':
    logging.basicConfig()
    run()

