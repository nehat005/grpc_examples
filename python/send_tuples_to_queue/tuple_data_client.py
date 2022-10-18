import grpc
import logging

import send_tuples_to_queue_pb2
import send_tuples_to_queue_pb2_grpc
import queue


class VisualizationQueue:
    def __init__(self):
        self.queue = queue.Queue(10)
        self.data_list = []

    def push_data(self, data):
        self.queue.put(data.queues.data)
        self.data_list.append(data.queues.data)
        self.print_list()

    def print_list(self):
        print('Items acquired: ', self.data_list, '\nNumber of Items: ', len(self.data_list))
        print('----------------------------------------------------------------------------')


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        visualization_queue = VisualizationQueue()

        stub = send_tuples_to_queue_pb2_grpc.SendDataStub(channel)
        response = stub.SingleData(send_tuples_to_queue_pb2.SendRequest(request_message='Send data to visualize'))
        response2 = stub.SingleDataAgain(send_tuples_to_queue_pb2.SendRequest(
            request_message='Send data AGAIN to visualize'))
        # print('Client Received: ', response)
        visualization_queue.push_data(response)
        visualization_queue.push_data(response2)


if __name__ == '__main__':
    logging.basicConfig()
    run()

