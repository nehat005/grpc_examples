from concurrent import futures
import logging

import grpc
import calculator_pb2
import calculator_pb2_grpc


class Calculate(calculator_pb2_grpc.CalculateServicer):

    def Multiply(self, request, context):
        return calculator_pb2.MultipliedReply(result=(request.number_1 * request.number_2))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculateServicer_to_server(Calculate(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
