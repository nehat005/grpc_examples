from __future__ import print_function

import logging
import grpc
import bidirectional_with_tuples_pb2
import bidirectional_with_tuples_pb2_grpc
# import queue

# data_queue = queue.Queue(maxsize=10)


# class Diarizer:
#     def __init__(self):
#         self.queue = queue.Queue(maxsize=10)
#
#     def put_data(self, input):
#         self.queue.put(input)
#         return self.queue


def send_queued_data(stub, input_data, speaker_name='Neha'):
    # speaker_name = input_data_[1]
    response = stub.SendDiarData(bidirectional_with_tuples_pb2.DataQueueRequest(
        data=bidirectional_with_tuples_pb2.DataList(timestamps=input_data)))
    print('Client Received: ', response.message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bidirectional_with_tuples_pb2_grpc.BidirectionalStub(channel)
        # diarizer = Diarizer()
        a = float(input('Enter timestamp: '))
        # b = input('Enter Name: ')
        # queued_data_to_send = diarizer.put_data([a, b])
        send_queued_data(stub, a)


if __name__ == '__main__':
    logging.basicConfig()
    run()
