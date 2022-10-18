from concurrent import futures
import grpc
import bidirectional_with_tuples_pb2_grpc
import bidirectional_with_tuples_pb2


class BidirectionalService(bidirectional_with_tuples_pb2_grpc.BidirectionalServicer):

    def SendDiarData(self, request_iterator, context):
        yield bidirectional_with_tuples_pb2.ReceivedMessage(message=" recieved")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bidirectional_with_tuples_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()