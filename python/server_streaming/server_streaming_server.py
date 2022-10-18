from concurrent import futures
import logging

import grpc
import server_streaming_pb2
import server_streaming_pb2_grpc


class SendData(server_streaming_pb2_grpc.SendDataServicer):

    def produce_tuples(self, timestamp, speaker_score, speaker_id):
        return server_streaming_pb2.SendResponse(queues=server_streaming_pb2.Queue(
            data=server_streaming_pb2.Queue.TimeData(timestamp=timestamp, speaker_score=speaker_score, speaker_name=speaker_id)))

    def StreamData(self, request, context):
        print('Client says:', request.request_message)
        times = [0.25, 0.5, 0.75, 1.0, 1.46, 1.98, 2.15, 2.45, 2.9, 3.3, 3.5, 3.8, 4.2, 4.5, 4.9, 5.3, 5.2, 5.25, 5.9, 6.8, 7.9, 8.2]
        speaker_ids = ['spkr_0', 'spkr_0','spkr_0', 'spkr_0', 'spkr_0',
                       'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1', 'spkr_1',
                       'spkr_0', 'spkr_0', 'spkr_0', 'spkr_0', 'spkr_0', 'spkr_0']
        speaker_score = [0.6, 0.8, 0.99, 0.8, 0.6,
                         0.2, 0.2, 0.2, 0.4, 0.4, 0.4, 0.2, 0.3, 0.5, 0.4, 0.4,
                         0.8, 0.8, 0.8, 1.0, 0.6, 0.8]
        for i in range(len(times)):
            tupled_data = self.produce_tuples(timestamp=times[i], speaker_score=speaker_score[i], speaker_id=speaker_ids[i])
            print('Sending Data iteration:  ', i, tupled_data)
            yield tupled_data


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_streaming_pb2_grpc.add_SendDataServicer_to_server(SendData(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
