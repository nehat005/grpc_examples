from concurrent import futures
import logging

import grpc
import send_data_pb2
import send_data_pb2_grpc


class SendData(send_data_pb2_grpc.SendDataServicer):

    def SingleData(self, request, context):
        print('Data Sent!')
        return send_data_pb2.SendResponse(queues=send_data_pb2.Queue(
            data=send_data_pb2.Queue.TimeData(timestamp=0.25, speaker_id='neha')))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    send_data_pb2_grpc.add_SendDataServicer_to_server(SendData(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
