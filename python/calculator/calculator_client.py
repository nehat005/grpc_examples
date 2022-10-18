import logging
import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculateStub(channel)
        a = int(input('Enter number 1: '))
        b = int(input('Enter number 2: '))
        response = stub.Multiply(calculator_pb2.MultiplyRequest(number_1=a, number_2=b))
        print('Client Received: ', response.result)


if __name__ == '__main__':
    logging.basicConfig()
    run()
