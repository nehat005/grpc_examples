from concurrent import futures
import grpc
import logging

import client_streaming_pb2
import client_streaming_pb2_grpc


def create_message(message):
    return client_streaming_pb2.SendRequest(queues=client_streaming_pb2.Queue(
                data=client_streaming_pb2.Queue.TimeData(timestamp=list(message)[0], speaker_score=list(message)[1],
                                                         speaker_name=list(message)[2])))


def message_iterator(message_list):
    for message in message_list:
        yield create_message(message)


class SendData:

    # def produce_tuples(self, timestamp, speaker_score, speaker_id):
    #     return client_streaming_pb2.SendRequest(queues=client_streaming_pb2.Queue(
    #         data=client_streaming_pb2.Queue.TimeData(timestamp=timestamp, speaker_score=speaker_score,
    #                                                  speaker_name=speaker_id)))

    def StreamData(self):
        times = [0.25, 0.5, 0.75, 1.0, 1.46, 1.98, 2.15, 2.45, 2.9, 3.3, 3.5, 3.8, 4.2, 4.5, 4.9, 5.2, 5.3, 5.34, 5.9,
                 6.8, 7.9, 8.2]
        speaker_ids = ['spkr_0', 'spkr_0', 'spkr_0', 'spkr_0', 'spkr_0',
                       'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1',
                       'spkr_1', 'spkr_1',
                       'spkr_0', 'spkr_0', 'spkr_0', 'spkr_0', 'spkr_0', 'spkr_0']
        speaker_score = [0.6, 0.8, 0.99, 0.8, 0.6,
                         0.2, 0.2, 0.2, 0.4, 0.4, 0.4, 0.2, 0.3, 0.5, 0.4, 0.4,
                         0.8, 0.8, 0.8, 1.0, 0.6, 0.8]
        for i in range(len(times)):
            yield [times[i], speaker_score[i], speaker_ids[i]]


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = client_streaming_pb2_grpc.SendDataStub(channel)
        s = SendData()
        list_of_requests = s.StreamData()

        response = stub.StreamData(message_iterator([x for x in list(list_of_requests)]))

        print("Server response: ", response.message)


if __name__ == '__main__':

    logging.basicConfig()
    run()
